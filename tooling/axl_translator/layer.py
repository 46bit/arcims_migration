import xml.etree.ElementTree as ET
from simple_renderer import SimpleRenderer
from value_map_renderer import ValueMapRenderer
from query import Query
from utils import pretty_xml

class Layer:
  def __init__(self, layer_name_prefix, layer_node):
    self.layer_node = layer_node
    self.type = self.layer_node.attrib["type"]
    self.id = int(self.layer_node.attrib["id"])
    self.layer_name = layer_name_prefix + str(self.id)

    d = self.layer_node.find("DATASET")
    if d is not None:
      self.dataset_name = d.attrib["name"].lower()
      self.dataset_type = d.attrib["type"].lower()

    if self.type == "featureclass":
      q = self.layer_node.find("QUERY")
      if q is not None:
        self.query = Query(q)

    self.renderers = []
    simple_renderer_nodes = self.layer_node.findall(".//SIMPLERENDERER")
    self.renderers += [SimpleRenderer(node) for node in simple_renderer_nodes]
    value_map_renderer_nodes = self.layer_node.findall(".//VALUEMAPRENDERER")
    self.renderers += [ValueMapRenderer(node) for node in value_map_renderer_nodes]

  def to_sql(self):
    q = "-- LAYER NAME \"{0}\"\nSELECT *".format(self.layer_name)

    # FROM
    tables = []
    if hasattr(self, "dataset_name"):
      tables += [self.dataset_name]
    if hasattr(self, "query"):
      tables += [self.query.tables()]
    if len(tables) == 0:
      return False
    q += " FROM " + ", ".join(["\"{}\"".format(t) for t in tables])

    # WHERE
    if hasattr(self, "query"):
      q += " WHERE {0}".format(self.query.where())

    return q# + ";"

  def to_css(self):
    css = "/* LAYER NAME {0} */\n".format(self.layer_name)
    for renderer in self.renderers:
      css += renderer.to_css()
    return css

  def to_sld(self):
    sld = ET.Element("StyledLayerDescriptor")
    sld.attrib["version"] = "1.0.0"
    sld.attrib["xsi:schemaLocation"] = "http://www.opengis.net/sld StyledLayerDescriptor.xsd"
    sld.attrib["xmlns"] = "http://www.opengis.net/sld"
    sld.attrib["xmlns:ogc"] = "http://www.opengis.net/ogc"
    sld.attrib["xmlns:xlink"] = "http://www.w3.org/1999/xlink"
    sld.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"

    named_layer = ET.SubElement(sld, "NamedLayer")
    name = ET.SubElement(named_layer, "Name")
    name.text = self.layer_name
    user_style = ET.SubElement(named_layer, "UserStyle")

    feature_type_style = ET.SubElement(user_style, "FeatureTypeStyle")
    for renderer in self.renderers:
      feature_type_style.extend(list(renderer.to_sld()))

    return pretty_xml(sld)

  def to_axl(self):
    return pretty_xml(self.layer_node)
