import sys, xml.etree.ElementTree as ET
import utils

class ValueMapRenderer:
  def __init__(self, node):
    self.node = node
    self.lookupfield = self.node.attrib["lookupfield"]

    self.classifiers = [c for c in node]
    self.symbols = [s for s in c for c in self.classifiers]

    """
    self.ensure_clauses_have_same_symbol
    # Verify all are SIMPLEsymbolSYMBOL xor SIMPLELINESYMBOL xor SIMPLEPOLYGONSYMBOL
    if not self.all_are(self.classifiers_symbols, self.classifiers_symbols[0].tag):
      # @TODO: More helpful output for cases we can't transform.
      # @TODO: Can potentially transform these cases?
      assert False

    if self.all_are(self.classifiers, "Exact"):

    elif self.all_are(self.classifiers, "Range"):

    elif self.exact_then_rest_are_range(self.classifiers):

    else:
      # @TODO: More helpful output for cases we can't transform.
      assert False
    """

  def all_are(self, classifiers, tag):
    ans = True
    for classifier in classifiers:
      ans |= classifier.tag == tag
    return ans

  def exact_then_rest_are_range(self, classifiers):
    ans = classifiers[0].tag == "Exact"
    ans |= self.all_are(classifiers[1:], "Range")
    return ans

  def to_css(self):
    css = ""
    for classifier in self.classifiers:
      css += self.classifier_to_css(classifier)
    return css

  def classifier_to_css(self, classifier):
    selector = self.classifier_conditions_to_css(classifier)
    symbol = classifier[0]
    symbolclass = utils.symbolclass_from_symbolnode(symbol)
    css = "/* CLASSIFIER INFO {0} */\n".format(str(classifier.attrib))
    if symbolclass:
      css += symbolclass.to_css(selector)
    return css + "\n"

  def classifier_conditions_to_css(self, classifier):
    selector = ""
    if classifier.tag == "EXACT":
      selector = "[{0} = \"{1}\"]".format(self.lookupfield, classifier.attrib["value"])
    elif classifier.tag == "RANGE":
      lower_bound = classifier.attrib["lower"]
      upper_bound = classifier.attrib["upper"]
      # @TODO: Switch based upon RANGE equality="upper"
      selector = "[{0} > {1}] [{0} <= {2}]".format(self.lookupfield, lower_bound, upper_bound)
    elif classifier.tag == "OTHER":
      sys.stderr.write("OTHER is not properly supported!\n")
      selector = "*"
    else:
      print classifier.tag
      assert False
    return selector

  def to_sld(self):
    feature_type_style = ET.Element("FeatureTypeStyle")
    for classifier in self.classifiers:
      rule = self.classifier_to_sld(classifier)
      feature_type_style.append(rule)
    return feature_type_style

  def classifier_to_sld(self, classifier):
    rule = ET.Element("Rule")

    fltr = self.classifier_conditions_to_sld(classifier)
    rule.append(fltr)

    symbolclass = utils.symbolclass_from_symbolnode(classifier[0])
    #css = "/* CLASSIFIER INFO {0} */\n".format(str(classifier.attrib))
    if symbolclass:
      symbolizer = symbolclass.to_sld()
      rule.append(symbolizer)

    return rule

  def classifier_conditions_to_sld(self, classifier):
    fltr = ET.Element("ogc:Filter")
    if classifier.tag == "EXACT":
      eqto = ET.SubElement(fltr, "ogc:PropertyIsEqualTo")
      propname = ET.SubElement(eqto, "ogc:PropertyName")
      propname.text = self.lookupfield
      propval = ET.SubElement(eqto, "ogc:Literal")
      propval.text = classifier.attrib["value"]
    elif classifier.tag == "RANGE":
      fltr_and = ET.SubElement(fltr, "ogc:And")

      gt = ET.SubElement(fltr_and, "ogc:PropertyIsGreaterThan")
      propname = ET.SubElement(gt, "ogc:PropertyName")
      propname.text = self.lookupfield
      propval = ET.SubElement(gt, "ogc:Literal")
      propval.text = classifier.attrib["lower"]

      lt = ET.SubElement(fltr_and, "ogc:PropertyIsLessThanOrEqualTo")
      propname = ET.SubElement(lt, "ogc:PropertyName")
      propname.text = self.lookupfield
      propval = ET.SubElement(lt, "ogc:Literal")
      propval.text = classifier.attrib["upper"]
    elif classifier.tag == "OTHER":
      sys.stderr.write("OTHER may not be properly supported!\n")
    else:
      print classifier.tag
      assert False
    return fltr

  def identify_differing_properties(self):
    diffs = []
    properties = self.clause_symbols[0].attrib
    for s in self.clause_symbols[1]:
      # @TODO: Unintenionally requires at least 2 clauses!
      for a_k, a_v in s.attrib:
        if a_k not in properties or a_v != properties[a_k]:
          diffs += [a_k]
    return diffs
