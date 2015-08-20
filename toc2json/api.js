"use strict"

var TOC = (function () {
  function TOC(a, name, b, gif) {
    this.a = a
    this.name = name
    this.b = b
    this.gif = gif
    this.layers = []
    this.groups = []
  }
  TOC.prototype.addLayer = function addLayer(layer) {
    this.layers.push(layer)
    return layer
  }
  TOC.prototype.addGroup = function addGroup(group) {
    this.groups.push(group)
    return group
  }
  return TOC
})()
exports.TOC = TOC

var GROUP = (function () {
  function GROUP(name, b) {
    this.name = name
    this.b = b
    this.layers = []
    this.groups = []
  }
  GROUP.prototype.addLayer = function addLayer(layer) {
    this.layers.push(layer)
    return layer
  }
  GROUP.prototype.addGroup = function addGroup(group) {
    this.groups.push(group)
    return group
  }
  return GROUP
})()
exports.GROUP = GROUP

var LAYER = function LAYER(code, name, gif, a, b, c, d) {
  this.code = code
  this.name = name
  this.gif = gif
  this.a = a
  this.b = b
  this.c = c
  this.d = d
}
exports.LAYER = LAYER
