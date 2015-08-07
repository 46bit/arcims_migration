import xml.etree.ElementTree as ET
import utils

class SimpleMarkerSymbol:
  def __init__(self, node):
    self.node = node

  def to_css(self, selector):
    # [MOCHK = 1] {
    css = selector + " {\n"
    # set mark, mark-size etc
    if "type" in self.node.attrib:
      mark = self.node.attrib["type"]
      css += "  mark: symbol({0});\n".format(mark)
    if "width" in self.node.attrib:
      size = self.node.attrib["width"]
      css += "  mark-size: {0}px;\n".format(size)
    css += "}\n"

    # [MOCHK = 1] :mark {
    css += selector + " :mark {\n"
    # set fill etc
    if "color" in self.node.attrib:
      color = utils.cs_rgb_to_hex(self.node.attrib["color"])
      css += "  fill: {0};\n".format(color)
    css += "}\n"

    return css

  def to_sld(self):
    point = ET.Element("PointSymbolizer")
    graphic = ET.SubElement(point, "Graphic")
    mark = ET.SubElement(graphic, "Mark") # @TODO: Check empty tag does nothing?

    if "type" in self.node.attrib:
      well_known_name = ET.SubElement(mark, "WellKnownName")
      well_known_name.text = self.node.attrib["type"]
    if "color" in self.node.attrib:
      fill = ET.SubElement(mark, "Fill")
      fillcolor = ET.SubElement(fill, "CssParameter")
      fillcolor.attrib["name"] = "fill"
      fillcolor.text = utils.cs_rgb_to_hex(self.node.attrib["color"])
    if "width" in self.node.attrib:
      size = ET.SubElement(graphic, "Size")
      size.text = self.node.attrib["width"] # @TODO: Size conversion?

    return point
