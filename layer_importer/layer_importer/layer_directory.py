import os

class LayerDirectory:
  def __init__(self, layer_dir):
    self.layer_dir = layer_dir
    assert os.path.exists(self.layer_dir)
    self.layer_name = os.path.basename(self.layer_dir)

  def axl(self):
    return self.read("axl")

  def sql(self):
    return self.read("sql")

  def css(self):
    return self.read("css")

  def sld(self):
    return self.read("sld")

  def read(self, extension):
    filename = self.layer_filepath(extension)
    with open(filename, "rb") as f:
      return f.read()

  def layer_filepath(self, extension):
    # @TODO: Trim self.output_dir of trailing slash for consistency
    return self.layer_dir + "/" + self.layer_name + "." + extension
