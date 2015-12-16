import xml.etree.ElementTree as ET
import utils

class SimplePolygonSymbol:
  def __init__(self, node):
    self.node = node

  def to_css(self, selector):
    css = selector + " {\n"
    if "fillcolor" in self.node.attrib:
      color = utils.cs_rgb_to_hex(self.node.attrib["fillcolor"])
      css += "  fill: {0};\n".format(color)
    if "boundary" in self.node.attrib and self.node.attrib["boundary"] == "true":
      if "boundarycolor" in self.node.attrib:
        color = utils.cs_rgb_to_hex(self.node.attrib["boundarycolor"])
        css += "  stroke: {0};\n".format(color)
      if "boundarywidth" in self.node.attrib:
        width = self.node.attrib["boundarywidth"]
        css += "  stroke-width: {0}px;\n".format(width)
    css += "}\n"

    return css

  def to_sld(self):
    poly = ET.Element("PolygonSymbolizer")
    fill = ET.SubElement(poly, "Fill")
    boundary = ET.SubElement(poly, "Stroke")

    if "fillcolor" in self.node.attrib:
      fillcolor = ET.SubElement(fill, "CssParameter")
      fillcolor.attrib["name"] = "fill"
      fillcolor.text = utils.cs_rgb_to_hex(self.node.attrib["fillcolor"])
      # @TODO: Opacities!
    if "boundary" in self.node.attrib and self.node.attrib["boundary"] == "true":
      if "boundarycolor" in self.node.attrib:
        boundarycolor = ET.SubElement(boundary, "CssParameter")
        boundarycolor.attrib["name"] = "stroke"
        boundarycolor.text = utils.cs_rgb_to_hex(self.node.attrib["boundarycolor"])
      if "boundarywidth" in self.node.attrib:
        boundarywidth = ET.SubElement(boundary, "CssParameter")
        boundarywidth.attrib["name"] = "stroke-width"
        boundarywidth.text = self.node.attrib["boundarywidth"] # @TODO: Size conversion?

    return poly
