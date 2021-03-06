import sys
import xml.etree.ElementTree as ET
import lxml.etree as etree
from simple_polygon_symbol import SimplePolygonSymbol
from simple_line_symbol import SimpleLineSymbol
from simple_marker_symbol import SimpleMarkerSymbol
from true_type_marker_symbol import TrueTypeMarkerSymbol

def cs_rgb_to_hex(cs_rgb):
  rgb = tuple([int(c) for c in cs_rgb.split(",")])
  return "#" + rgb_to_hex(rgb)

# https://pythonjunkie.wordpress.com/2012/07/19/convert-hex-color-values-to-
# rgb-in-python/ (very tidy)
def rgb_to_hex(rgb):
  return '%02x%02x%02x' % rgb

def symbolclass_from_symbolnode(symbolnode):
  if symbolnode.tag == "SIMPLEPOLYGONSYMBOL":
    return SimplePolygonSymbol(symbolnode)
  elif symbolnode.tag == "SIMPLELINESYMBOL":
    return SimpleLineSymbol(symbolnode)
  elif symbolnode.tag == "SIMPLEMARKERSYMBOL":
    return SimpleMarkerSymbol(symbolnode)
  elif symbolnode.tag == "TRUETYPEMARKERSYMBOL":
    return TrueTypeMarkerSymbol(symbolnode)
  else:
    sys.stderr.write("{0} is not supported!\n".format(symbolnode.tag))
    return False

def pretty_xml(x):
  sld_string = ET.tostring(x, encoding="utf8", method="xml")
  parser = etree.XMLParser(remove_blank_text=True)
  return etree.tostring(etree.fromstring(sld_string, parser), pretty_print = True)

def columnref_to_columnname(cr):
  return cr.split(".")[-1]
