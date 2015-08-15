// ECMASCRIPT 6
// http://babeljs.io/docs/usage/cli/
// COMPILE WITH
//   babel api.js > api-compiled.js

class TOCElement {
  constructor() {
    this.layers = []
    this.groups = []
  }
  addLayer(layer) {
    this.layers.push(layer)
    return layer
  }
  addGroup(group) {
    this.groups.push(group)
    return group
  }
}

export class TOC extends TOCElement {
  constructor(a, name, b, gif) {
    super()
    this.a = a
    this.name = name
    this.b = b
    this.gif = gif
  }
}

export class GROUP extends TOCElement {
  constructor(name, b) {
    super()
    this.name = name
    this.b = b
  }
}

export class LAYER {
  constructor(code, name, gif, a, b, c, d) {
    this.code = code
    this.name = name
    this.gif = gif
    this.a = a
    this.b = b
    this.c = c
    this.d = d
  }
}
