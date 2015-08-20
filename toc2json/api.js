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
  return LAYER
})()
exports.LAYER = LAYER
