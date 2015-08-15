import json, requests

# curl -u admin:geoserver -XPOST -H 'Content-type: application/json' -d 'json data' http://localhost:8080/geoserver/rest/styles

class GeoserverApi:
  def __init__(self, api_url="http://localhost:8080/geoserver", api_username="admin", api_password="geoserver"):
    self.api_url = api_url
    self.api_username = api_username
    self.api_password = api_password

  def full_url(self, endpoint):
    return self.api_url + endpoint

  def request(self, method, endpoint, payload, headers={}):
    endpoint_url = self.full_url(endpoint)
    defaults = {"content-type": "application/json"}
    defaults.update(headers)
    r = requests.request(method, endpoint_url, auth=(self.api_username, self.api_password), headers=defaults, data=payload)
    print "REQUEST(" + r.url + ", " + payload + ") =", r.status_code, r.text
    return r

  def get(self, endpoint, payload="", headers={}):
    return self.request('GET', endpoint, payload, headers)

  def post(self, endpoint, payload="", headers={}):
    return self.request('POST', endpoint, payload, headers)

  def put(self, endpoint, payload="", headers={}):
    return self.request('PUT', endpoint, payload, headers)

  def delete(self, endpoint, payload="", headers={}):
    return self.request('DELETE', endpoint, payload, headers)

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
