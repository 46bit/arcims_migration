#!/usr/bin/env node

// node toc2json.js ../taesp_ahrc_2007/taesp_100.toc

var fs = require("fs")
var path = require("path")
var assert = require("assert")

var api = require(process.argv[2])//'./api_openlayers.js')
TOC = api.TOC
GROUP = api.GROUP
LAYER = api.LAYER

// http://stackoverflow.com/a/20473643/392331
function read(f) {
  return fs.readFileSync(f).toString();
}
function include(f) {
  eval.apply(global, [read(f)]);
}

tocfilepath = process.argv[3] //'./taesp_100.toc.js'
console.error("(Processing TOC file " + String(tocfilepath) + ")")

toc = false
include(tocfilepath)
assert(toc, "TOC was not set by the TOC file. Investigate!")

var toc_info = {
  filepath: tocfilepath,
  filename: path.resolve(tocfilepath),
  toc: toc
}
console.log(JSON.stringify(toc_info, null, 2))
