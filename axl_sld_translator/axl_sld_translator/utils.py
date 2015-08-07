import sys
from simple_polygon_symbol import SimplePolygonSymbol
from simple_line_symbol import SimpleLineSymbol
from simple_marker_symbol import SimpleMarkerSymbol

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
  else:
    sys.stderr.write("{0} is not supported!\n".format(symbolnode.tag))
    return False
