import json
from layer import Layer

# curl -u admin:geoserver -XPOST -H 'Content-type: application/json' -d 'json data' http://localhost:8080/geoserver/rest/styles

class GeoserverApi:
  def __init__(self, api_url="http://localhost:8080/geoserver", api_username="admin", api_password="geoserver"):
    self.api_url = api_url
    self.api_username = api_username
    self.api_password = api_password

  def request(self, method, endpoint, payload):
    endpoint_url = self.api_url + endpoint
    return requests.get(endpoint_url, auth=(self.api_username, self.api_password))

  def get(self, endpoint, payload):
    return self.request('GET', endpoint, payload)

  def post(self, endpoint, payload):
    return self.request('POST', endpoint, payload)

  def put(self, endpoint, payload):
    return self.request('PUT', endpoint, payload)

  def delete(self, endpoint, payload):
    return self.request('DELETE', endpoint, payload)

  def create_layer(self, layer):
    pass

  def create_style(self, name, style_payload):
    filename = name + "." + format
    style = {
      "name": name,
      "format": "sld",
      "filename": filename
    }
    post("/rest/styles.json", json.dumps(style)) # @TODO: Handle errors!

    put("/rest/styles/" + name, style_payload, {"Content-type": "application/vnd.ogc.sld+xml"}) # @TODO: Handle errors!
