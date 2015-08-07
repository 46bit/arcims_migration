class Query:
  def __init__(self, query_node):
    self.query_node = query_node

  def where(self):
    clauses = []
    if len(self.join()) > 0: clauses += [self.join().lower()]
    if "where" in self.query_node.attrib and len(self.query_node.attrib["where"]) > 0:
      clauses += [self.query_node.attrib["where"].lower()]
    return " AND ".join(clauses)

  def tables(self):
    return self.query_node.attrib["jointables"].lower() if "jointables" in self.query_node.attrib else ""

  def join(self):
    # joinexpression="To=[tp_POSI.POSI_NO],From=[tblPOSIRec.POSINO],Type=[exact]"
    if "joinexpression" not in self.query_node.attrib: ""
    clauses = dict([item.split("=") for item in self.query_node.attrib["joinexpression"].split(",")])
    assert clauses["Type"] == "[exact]"
    assert clauses["To"][0] == "["
    assert clauses["To"][-1] == "]"
    assert clauses["From"][0] == "["
    assert clauses["From"][-1] == "]"

    # "tp_posi.posi_no = tblposirec.posino"
    return " = ".join([clauses["To"][1:-1], clauses["From"][1:-1]]).lower()
