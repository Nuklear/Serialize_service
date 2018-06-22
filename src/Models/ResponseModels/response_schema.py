response_schema = {
  "$id": "http://example.com/example.json",
  "type": "object",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "properties": {
    "workspaceId": {
      "$id": "/properties/workspaceId",
      "type": "string",
      "title": "The Workspaceid Schema ",
      "default": "",
      "examples": [
        "5b0eb5a5002bc52b25bdf276"
      ]
    },
    "validationActId": {
      "$id": "/properties/validationActId",
      "type": "string",
      "title": "The Validationactid Schema ",
      "default": "",
      "examples": [
        "5b0ebd2e002bc53bac7bbfea"
      ]
    },
    "measurementSystemResult": {
      "$id": "/properties/measurementSystemResult",
      "type": "object",
      "properties": {
        "results": {
          "$id": "/properties/measurementSystemResult/properties/results",
          "type": "array",
          "items": {
            "$id": "/properties/measurementSystemResult/properties/results/items",
            "type": "object",
            "properties": {
              "characteristicId": {
                "$id": "/properties/measurementSystemResult/properties/results/items/properties/characteristicId",
                "type": "string",
                "title": "The Characteristicid Schema ",
                "default": "",
                "examples": [
                  "0a662382-6c1e-4386-8128-ee0f4b9a1ec9"
                ]
              },
              "iso": {
                "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso",
                "type": "object",
                "properties": {
                  "qms": {
                    "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/qms",
                    "type": "integer",
                    "title": "The Qms Schema ",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  },
                  "outliers": {
                    "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/outliers",
                    "type": "integer",
                    "title": "The Outliers Schema ",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  },
                  "uncertainties": {
                    "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties",
                    "type": "array",
                    "items": {
                      "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties/items",
                      "type": "object",
                      "properties": {
                        "name": {
                          "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/name",
                          "type": "null",
                          "title": "The Name Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "value": {
                          "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/value",
                          "type": "null",
                          "title": "The Value Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "manualInput": {
                          "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/manualInput",
                          "type": "null",
                          "title": "The Manualinput Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "active": {
                          "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/active",
                          "type": "null",
                          "title": "The Active Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "notes": {
                          "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/notes",
                          "type": "null",
                          "title": "The Notes Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        }
                      }
                    }
                  },
                  "ssigma": {
                    "$id": "/properties/measurementSystemResult/properties/results/items/properties/iso/properties/ssigma",
                    "type": "null",
                    "title": "The Ssigma Schema ",
                    "default": None,
                    "examples": [
                      None
                    ]
                  }
                }
              },
              "msa": {
                "$id": "/properties/measurementSystemResult/properties/results/items/properties/msa",
                "type": "null",
                "title": "The Msa Schema ",
                "default": None,
                "examples": [
                  None
                ]
              },
              "vda": {
                "$id": "/properties/measurementSystemResult/properties/results/items/properties/vda",
                "type": "null",
                "title": "The Vda Schema ",
                "default": None,
                "examples": [
                  None
                ]
              }
            }
          }
        }
      }
    },
    "measurementProcessResult": {
      "$id": "/properties/measurementProcessResult",
      "type": "object",
      "properties": {
        "results": {
          "$id": "/properties/measurementProcessResult/properties/results",
          "type": "array",
          "items": {
            "$id": "/properties/measurementProcessResult/properties/results/items",
            "type": "object",
            "properties": {
              "characteristicId": {
                "$id": "/properties/measurementProcessResult/properties/results/items/properties/characteristicId",
                "type": "string",
                "title": "The Characteristicid Schema ",
                "default": "",
                "examples": [
                  "0a662382-6c1e-4386-8128-ee0f4b9a1ec9"
                ]
              },
              "iso": {
                "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso",
                "type": "object",
                "properties": {
                  "qmp": {
                    "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/qmp",
                    "type": "integer",
                    "title": "The Qmp Schema ",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  },
                  "uncertainties": {
                    "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties",
                    "type": "array",
                    "items": {
                      "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties/items",
                      "type": "object",
                      "properties": {
                        "name": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/name",
                          "type": "null",
                          "title": "The Name Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "value": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/value",
                          "type": "null",
                          "title": "The Value Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "manualInput": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/manualInput",
                          "type": "null",
                          "title": "The Manualinput Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "active": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/active",
                          "type": "null",
                          "title": "The Active Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        },
                        "notes": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/uncertainties/items/properties/notes",
                          "type": "null",
                          "title": "The Notes Schema ",
                          "default": None,
                          "examples": [
                            None
                          ]
                        }
                      }
                    }
                  },
                  "graphPoints": {
                    "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/graphPoints",
                    "type": "array",
                    "items": {
                      "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/graphPoints/items",
                      "type": "object",
                      "properties": {
                        "level": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/graphPoints/items/properties/level",
                          "type": "integer",
                          "title": "The Level Schema ",
                          "default": 0,
                          "examples": [
                            0
                          ]
                        },
                        "character": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/graphPoints/items/properties/character",
                          "type": "string",
                          "title": "The Character Schema ",
                          "default": "",
                          "examples": [
                            "0"
                          ]
                        },
                        "number": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/graphPoints/items/properties/number",
                          "type": "integer",
                          "title": "The Number Schema ",
                          "default": 0,
                          "examples": [
                            0
                          ]
                        },
                        "value": {
                          "$id": "/properties/measurementProcessResult/properties/results/items/properties/iso/properties/graphPoints/items/properties/value",
                          "type": "integer",
                          "title": "The Value Schema ",
                          "default": 0,
                          "examples": [
                            0
                          ]
                        }
                      }
                    }
                  }
                }
              },
              "msa": {
                "$id": "/properties/measurementProcessResult/properties/results/items/properties/msa",
                "type": "null",
                "title": "The Msa Schema ",
                "default": None,
                "examples": [
                  None
                ]
              },
              "vda": {
                "$id": "/properties/measurementProcessResult/properties/results/items/properties/vda",
                "type": "null",
                "title": "The Vda Schema ",
                "default": None,
                "examples": [
                  None
                ]
              }
            }
          }
        }
      }
    }
  }
}
