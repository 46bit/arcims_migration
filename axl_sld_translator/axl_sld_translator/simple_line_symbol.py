import xml.etree.ElementTree as ET
import utils

class SimpleLineSymbol:
  def __init__(self, node):
    self.node = node

  def to_css(self, selector):
    css = selector + " {\n"
    if "color" in self.node.attrib:
      color = utils.cs_rgb_to_hex(self.node.attrib["color"])
      css += "  stroke: {0};\n".format(color)
    if "width" in self.node.attrib:
      width = self.node.attrib["width"]
      css += "  stroke-width: {0}px;\n".format(width)
    css += "  stroke-linecap: round;\n"
    css += "}\n"

    return css

  def to_sld(self):
    line = ET.Element("LineSymbolizer")
    stroke = ET.SubElement(line, "Stroke")

    if "color" in self.node.attrib:
      strokecolor = ET.SubElement(stroke, "CssParameter")
      strokecolor.attrib["name"] = "stroke"
      strokecolor.text = utils.cs_rgb_to_hex(self.node.attrib["color"])
    if "width" in self.node.attrib:
      strokewidth = ET.SubElement(stroke, "CssParameter")
      strokewidth.attrib["name"] = "stroke-width"
      strokewidth.text = self.node.attrib["width"] # @TODO: Size conversion?

    return line
