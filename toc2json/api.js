"use strict"

var TOC = (function () {
  function TOC(a, name, b, gif) {
    this.element_type = "TOC"
    this.a = a
    this.name = name
    this.b = b
    this.gif = gif
    this.layersAndGroups = []
  }
  TOC.prototype.addLayer = function addLayer(layer) {
    this.layersAndGroups.push(layer)
    return layer
  }
  TOC.prototype.addGroup = function addGroup(group) {
    this.layersAndGroups.push(group)
    return group
  }
  TOC.prototype.asOpenLayers = function asOpenLayers(source_constructor) {
    var mapped = []
    for (var i in this.layersAndGroups) {
      var layerOrGroup = this.layersAndGroups[i]
      if (typeof layerOrGroup !== "LAYER" || layerOrGroup.codeIsNumeric()) {
        var olLayerOrGroup = layerOrGroup.asOpenLayers(source_constructor)
        mapped.push(olLayerOrGroup)
      }
    }
    return mapped
  }
  return TOC
})()
exports.TOC = TOC

var GROUP = (function () {
  function GROUP(name, b) {
    this.element_type = "GROUP"
    this.name = name
    this.b = b
    this.layersAndGroups = []
  }
  GROUP.prototype.addLayer = function addLayer(layer) {
    this.layersAndGroups.push(layer)
    return layer
  }
  GROUP.prototype.addGroup = function addGroup(group) {
    this.layersAndGroups.push(group)
    return group
  }
  GROUP.prototype.asOpenLayers = function asOpenLayers(source_constructor) {
    var mapped = []
    for (var i in this.layersAndGroups) {
      var layerOrGroup = this.layersAndGroups[i]
      if (typeof layerOrGroup !== "LAYER" || layerOrGroup.codeIsNumeric()) {
        var olLayerOrGroup = layerOrGroup.asOpenLayers(source_constructor)
        mapped.push(olLayerOrGroup)
      }
    }
    var olGroup = new ol.layer.Group({
      title: this.name,
      layers: mapped
    })
    return olGroup
  }
  return GROUP
})()
exports.GROUP = GROUP

var LAYER = (function () {
  function LAYER(code, name, gif, a, b, c, visible) {
    this.element_type = "LAYER"
    this.code = code
    this.name = name
    this.gif = gif
    this.a = a
    this.b = b
    this.c = c
    this.visible = visible
  }
  LAYER.prototype.codeIsNumeric = function codeIsNumeric() {
    return String(parseInt(this.code, 10)) == this.code
  }
  LAYER.prototype.asOpenLayers = function asOpenLayers(source_constructor) {
    var olSource = source_constructor(this.code)
    var olLayer = new ol.layer.Image({
      title: this.name,
      visible: !!this.visible,
      source: olSource
    })
    return olLayer
  }
  return LAYER
})()
exports.LAYER = LAYER
