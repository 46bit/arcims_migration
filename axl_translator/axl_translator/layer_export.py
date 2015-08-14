import os
from layer import Layer

class LayerExport:
  def __init__(self, output_dir, layer):
    self.layer = layer
    self.output_dir = output_dir
    self.output_layer_dir = self.output_dir + "/" + self.layer.layer_name

  def export_directory(self):
    if not os.path.exists(self.output_layer_dir):
      os.makedirs(self.output_layer_dir)

  def export_axl(self):
    # @TODO: Put the Layer XML in a .xml or .axl file in the directory.
    filename = self.layer_filename("axl")
    self.export(filename, self.layer.to_axl())
    return filename

  def export_sql(self):
    filename = self.layer_filename("sql")
    self.export(filename, self.layer.to_sql())
    return filename

  def export_css(self):
    filename = self.layer_filename("css")
    self.export(filename, self.layer.to_css())
    return filename

  def export_sld(self):
    filename = self.layer_filename("sld")
    self.export(filename, self.layer.to_sld())
    return filename

  def export(self, filename, data):
    self.export_directory()
    with open(filename, "w+b") as f:
      f.write(data)

  def layer_filename(self, extension):
    # @TODO: Trim self.output_dir of trailing slash for consistency
    return self.output_layer_dir + "/" + self.layer.layer_name + "." + extension
