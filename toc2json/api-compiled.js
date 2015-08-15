// ECMASCRIPT 6
// http://babeljs.io/docs/usage/cli/
// COMPILE WITH
//   babel api.js > api-compiled.js

"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var TOC = (function () {
  function TOC(a, name, b, gif) {
    _classCallCheck(this, TOC);

    this.a = a;
    this.name = name;
    this.b = b;
    this.gif = gif;
    this.layers = [];
    this.groups = [];
  }

  _createClass(TOC, [{
    key: "addLayer",
    value: function addLayer(layer) {
      this.layers.push(layer);
      return layer;
    }
  }, {
    key: "addGroup",
    value: function addGroup(group) {
      this.groups.push(group);
      return group;
    }
  }]);

  return TOC;
})();

exports.TOC = TOC;

var GROUP = (function () {
  function GROUP(name, b) {
    _classCallCheck(this, GROUP);

    this.name = name;
    this.b = b;
    this.layers = [];
    this.groups = [];
  }

  _createClass(GROUP, [{
    key: "addLayer",
    value: function addLayer(layer) {
      this.layers.push(layer);
      return layer;
    }
  }, {
    key: "addGroup",
    value: function addGroup(group) {
      this.groups.push(group);
      return group;
    }
  }]);

  return GROUP;
})();

exports.GROUP = GROUP;

var LAYER = function LAYER(code, name, gif, a, b, c, d) {
  _classCallCheck(this, LAYER);

  this.code = code;
  this.name = name;
  this.gif = gif;
  this.a = a;
  this.b = b;
  this.c = c;
  this.d = d;
};

exports.LAYER = LAYER;

