import json, requests, os
from subprocess import call

# curl -u admin:geoserver -XPOST -H 'Content-type: application/json' -d 'json data' http://localhost:8080/geoserver/rest/styles

class GeoserverApi:
  def __init__(self, api_url="http://localhost:8080/geoserver", api_username="admin", api_password="geoserver"):
    self.api_url = api_url
    self.api_username = api_username
    self.api_password = api_password

  def full_url(self, endpoint):
    return self.api_url + endpoint

  def request(self, method, endpoint, payload, headers={}, files={}):
    endpoint_url = self.full_url(endpoint)
    defaults = {"content-type": "application/json"}
    defaults.update(headers)
    r = requests.request(method, endpoint_url, auth=(self.api_username, self.api_password), headers=defaults, data=payload, files=files)
    print "REQUEST(" + r.url + ", " + payload + ") =", r.status_code, r.text
    return r

  def get(self, endpoint, payload="", headers={}):
    return self.request('GET', endpoint, payload, headers)

  def post(self, endpoint, payload="", headers={}):
    return self.request('POST', endpoint, payload, headers)

  def put(self, endpoint, payload="", headers={}, files={}):
    return self.request('PUT', endpoint, payload, headers, files)

  def delete(self, endpoint, payload="", headers={}):
    return self.request('DELETE', endpoint, payload, headers)

  def delete_workspace(self, workspace, recurse=False):
    endpoint = "/rest/workspaces/{0}.json".format(workspace)
    endpoint += "?recurse={0}".format(recurse)
    print self.delete(endpoint)

  def create_workspace(self, workspace):
    workspace = {
      "workspace": {
        "name": workspace
      }
    }
    print self.post("/rest/workspaces.json", json.dumps(workspace))

  def create_postgis_datastore(self, workspace, datastore, db_host, db_port, db_name, db_user, db_password, schema="public"):
    datastore = {
      "dataStore": {
        "name": datastore,
        "type": "PostGIS",
        "connectionParameters": {
          "schema": schema,
          "host": db_host,
          "port": db_port,
          "database": db_name,
          "user": db_user,
          "passwd": db_password,
          "dbtype": "postgis"
        }
      }
    }
    endpoint = "/rest/workspaces/{0}/datastores.json".format(workspace)
    print self.post(endpoint, json.dumps(datastore))

  def create_postgis_featuretype(self, workspace, datastore, name, srs):
    featuretype = {
      "featureType": {
        "name": name,
        "title": name,
        "srs": srs,
        "enabled": True
      }
    }
    endpoint = "/rest/workspaces/{0}/datastores/{1}/featuretypes.json?recalculate=nativebbox,latlonbbox"
    print self.post(endpoint.format(workspace, datastore), json.dumps(featuretype)) # @TODO: Handle errors!

  def create_style(self, workspace, name, sld):
    style = {
      "style": {
        "name": name,
        "format": "sld",
        "filename": "{0}.sld".format(name)
      }
    }
    print self.post("/rest/workspaces/{0}/styles.json".format(workspace), json.dumps(style)) # @TODO: Handle errors!

    print self.put("/rest/workspaces/{0}/styles/".format(workspace) + name, sld, {"content-type": "application/vnd.ogc.sld+xml"}) # @TODO: Handle errors!

  def set_layer_style(self, workspace, name, style):
    url = "/rest/layers/{}.json".format(name)
    layer = self.get(url).json() # @TODO: Handle errors!
    style_endpoint = "/rest/workspaces/{0}/styles/{1}.json".format(workspace, style)
    layer["layer"]["defaultStyle"] = {
      "workspace": workspace,
      "href": self.full_url(style_endpoint),
      "name": style
    }
    print self.put(url, json.dumps(layer)) # @TODO: Handle errors!

  def create_geotiff_store_layer(self, workspace, name, geotiff_path):
    endpoint = "/rest/workspaces/{0}/coveragestores/{1}/file.geotiff?coverageName={1}"
    with open(geotiff_path, "rb") as f:
      print self.put(endpoint.format(workspace, name), "", {"Content-type": "image/tiff"}, {"file": f})

  def create_worldfile_geotiff_store_layer(self, workspace, name, geotiff_path, worldfile_path, prj_path):
    tmp_zip_path = "/tmp/{0}.zip".format(name)

    print ">> Zipping ({0}, {1}, {2}) into temporary {3}".format(geotiff_path, worldfile_path, prj_path, tmp_zip_path)
    call(["zip", "-rj", tmp_zip_path, geotiff_path, worldfile_path, prj_path])

    endpoint = "/rest/workspaces/{0}/coveragestores/{1}/file.worldimage?coverageName={1}"
    print ">> Submitting to {0}".format(endpoint)
    with open(tmp_zip_path, "rb") as f:
      print self.put(endpoint.format(workspace, name), "", {"content-type": "application/zip"}, {"file": f})

    #print ">> Erasing temporary {0}".format(tmp_zip_path)
    #call(["rm", tmp_zip_path])
