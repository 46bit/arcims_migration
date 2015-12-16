import json, requests, os, time
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
    print "REQUEST(" + r.url + ", " + payload + ", " + str(defaults) + ") =", r.status_code, r.text
    return r

  def get(self, endpoint, payload="", headers={}):
    return self.request('GET', endpoint, payload, headers)

  def post(self, endpoint, payload="", headers={}):
    return self.request('POST', endpoint, payload, headers)

  def put(self, endpoint, payload="", headers={}, files={}):
    return self.request('PUT', endpoint, payload, headers, files)

  def delete(self, endpoint, payload="", headers={}):
    return self.request('DELETE', endpoint, payload, headers)

  def curl(self, endpoint, segments):
    segments = ["curl", "-u", "{0}:{1}".format(self.api_username, self.api_password)] + segments + [self.full_url(endpoint)]
    return call(segments)

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

  def create_postgis_featuretype(self, workspace, datastore, name, native_name, srs):
    featuretype = {
      "featureType": {
        "name": name,
        "nativeName": native_name,
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
    endpoint = "/rest/workspaces/{0}/coveragestores/{1}/file.geotiff".format(workspace, name)
    print self.curl(endpoint, ["-X", "PUT", "-H", "Content-type:image/tiff", "--data-binary", "@{}".format(os.path.abspath(geotiff_path))])

  def create_worldfile_geotiff_store_layer(self, workspace, name, tiff_path, worldfile_path, prj_path, projection):
    tmp_folder = os.path.dirname(tiff_path) + "/out"
    print call(["mkdir", "-p", tmp_folder])

    tmp_tiff_path = tmp_folder + "/{0}.tif".format(name)
    tmp_worldfile_path = tmp_folder + "/{0}.tfw".format(name)
    tmp_prj_path = tmp_folder + "/{0}.prj".format(name)
    print call(["cp", tiff_path, tmp_tiff_path])
    print call(["cp", worldfile_path, tmp_worldfile_path])
    print call(["cp", prj_path, tmp_prj_path])

    tmp_geotiff_path = tmp_folder + "/{0}-geotiff.tif".format(name)
    print call(["gdal_translate", "-of", "GTiff", "-a_srs", projection, tmp_tiff_path, tmp_geotiff_path])

    print self.create_geotiff_store_layer(workspace, name, tmp_geotiff_path)

    payload = '{"coverage": {"srs": "' + projection + '", "projectionPolicy": "FORCE_DECLARED", "enabled": true}}'
    endpoint = "/rest/workspaces/{0}/coveragestores/{1}/coverages/{1}.json".format(workspace, name)
    print self.put(endpoint, payload)

    #print call(["rm", "-rf", tmp_folder])

  def delete_coveragestore(self, workspace, coveragestore, recurse=False):
    endpoint = "/rest/workspaces/{0}/coveragestores/{1}.json".format(workspace, coveragestore)
    endpoint += "?recurse={0}".format(recurse)
    print self.delete(endpoint)

  def create_layergroup_from_layers(self, workspace, layergroup_name, layer_names):
    layergroup = {
      "layerGroup": {
        "name": layergroup_name,
        "workspace": {
          "name": workspace
        },
        "mode": "SINGLE",
        "publishables": {
          "published": []
        }
      }
    }

    for layer_name in layer_names:
      layergroup["layerGroup"]["publishables"]["published"].append({
        "name": layer_name
        #,
        #"@type": "layer"
      })

    print self.post("/rest/workspaces/{0}/layergroups.json".format(workspace), json.dumps(layergroup)) # @TODO: Handle errors!
