import xml.etree.ElementTree as ET
import utils

class SimpleRenderer:
  def __init__(self, simple_renderer_node):
    self.node = simple_renderer_node
    #print_tree(self.simple_renderer_node)

    self.symbols = [s for s in self.node]

  def to_css(self):
    css = ""
    for symbol in self.symbols:
      symbolclass = utils.symbolclass_from_symbolnode(symbol)
      if symbolclass:
        css += symbolclass.to_css("*")
    return css

  def to_sld(self):
    feature_type_style = ET.Element("FeatureTypeStyle")
    for symbol in self.symbols:
      rule = ET.SubElement(feature_type_style, "Rule")
      symbolclass = utils.symbolclass_from_symbolnode(symbol)
      if symbolclass:
        symbolizer = symbolclass.to_sld()
        rule.append(symbolizer)
    return feature_type_style
