import xml.etree.ElementTree as ET
import utils

class TrueTypeMarkerSymbol:
  def __init__(self, node):
    self.node = node

  def to_css(self, selector):
    raise "TrueTypeMarkerSymbol lacks CSS output for now."

  def to_sld(self):
    point = ET.Element("PointSymbolizer")
    graphic = ET.SubElement(point, "Graphic")
    mark = ET.SubElement(graphic, "Mark") # @TODO: Check empty tag does nothing?

    if "font" in self.node.attrib and "character" in self.node.attrib:
      well_known_name = ET.SubElement(mark, "WellKnownName")
      # {:X} outputs the character code in hex. GeoServer documentation is ambiguous on whether we need to.
      well_known_name.text = "ttf://{}#0x{:X}".format(self.node.attrib["font"], int(self.node.attrib["character"]))
    if "fontcolor" in self.node.attrib:
      fill = ET.SubElement(mark, "Fill")
      fillcolor = ET.SubElement(fill, "CssParameter")
      fillcolor.attrib["name"] = "fill"
      fillcolor.text = utils.cs_rgb_to_hex(self.node.attrib["fontcolor"])
    if "fontsize" in self.node.attrib:
      size = ET.SubElement(graphic, "Size")
      size.text = self.node.attrib["fontsize"] # @TODO: Size conversion?

    return point
