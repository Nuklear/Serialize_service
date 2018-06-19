request_schema = {
    "$ref": "#/definitions/Responce",
    "definitions": {
        "Responce": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "workspaceId": {
                    "type": "string"
                },
                "validationActId": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "creationDate": {
                    "type": "integer"
                },
                "creatorId": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                },
                "lastEdited": {
                    "type": "integer"
                },
                "defaultEvaluationMethod": {
                    "type": "null"
                },
                "measurementTask": {
                    "$ref": "#/definitions/MeasurementTask"
                },
                "measurementSystem": {
                    "$ref": "#/definitions/MeasurementSystem"
                },
                "measurementProcess": {
                    "$ref": "#/definitions/MeasurementProcess"
                },
                "experimentType1Data": {
                    "$ref": "#/definitions/ExperimentType1Data"
                },
                "experimentType2Data": {
                    "$ref": "#/definitions/ExperimentType2Data"
                }
            },
            "required": [
                "creationDate",
                "creatorId",
                "defaultEvaluationMethod",
                "experimentType1Data",
                "experimentType2Data",
                "lastEdited",
                "measurementProcess",
                "measurementSystem",
                "measurementTask",
                "name",
                "status",
                "validationActId",
                "workspaceId"
            ],
            "title": "Responce"
        },
        "ExperimentType1Data": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "table": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/ExperimentType1DataTable"
                    }
                }
            },
            "required": [
                "table"
            ],
            "title": "ExperimentType1Data"
        },
        "ExperimentType1DataTable": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristicId": {
                    "type": "string"
                },
                "cells": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/PurpleCell"
                    }
                },
                "u_ENV": {
                    "type": "null"
                }
            },
            "required": [
                "cells",
                "characteristicId",
                "u_ENV"
            ],
            "title": "ExperimentType1DataTable"
        },
        "PurpleCell": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "repetition": {
                    "type": "integer"
                },
                "masterObjectId": {
                    "$ref": "#/definitions/MasterObjectID"
                },
                "value": {
                    "type": "number"
                }
            },
            "required": [
                "masterObjectId",
                "repetition",
                "value"
            ],
            "title": "PurpleCell"
        },
        "ExperimentType2Data": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "tableConstructionMethod": {
                    "type": "string"
                },
                "table": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/ExperimentType2DataTable"
                    }
                }
            },
            "required": [
                "table",
                "tableConstructionMethod"
            ],
            "title": "ExperimentType2Data"
        },
        "ExperimentType2DataTable": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristicId": {
                    "type": "string"
                },
                "cells": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/FluffyCell"
                    }
                },
                "u_AV": {
                    "type": "null"
                }
            },
            "required": [
                "cells",
                "characteristicId",
                "u_AV"
            ],
            "title": "ExperimentType2DataTable"
        },
        "FluffyCell": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "level": {
                    "type": "integer"
                },
                "part": {
                    "type": "integer"
                },
                "repetition": {
                    "type": "integer"
                },
                "value": {
                    "type": "integer"
                }
            },
            "required": [
                "level",
                "part",
                "repetition",
                "value"
            ],
            "title": "FluffyCell"
        },
        "MeasurementProcess": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristics": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/MeasurementProcessCharacteristic"
                    }
                }
            },
            "required": [
                "characteristics"
            ],
            "title": "MeasurementProcess"
        },
        "MeasurementProcessCharacteristic": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristicId": {
                    "type": "string"
                },
                "greatestInfluenceFactor": {
                    "type": "string"
                },
                "uncertainties": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Uncertainty"
                    }
                },
                "temperatureInfluence": {
                    "type": "boolean"
                },
                "temperatureInfluenceMethod": {
                    "type": "string"
                },
                "temperatureInfluenceParams": {
                    "$ref": "#/definitions/TemperatureInfluenceParams"
                },
                "material": {
                    "type": "string"
                }
            },
            "required": [
                "characteristicId",
                "greatestInfluenceFactor",
                "material",
                "temperatureInfluence",
                "temperatureInfluenceMethod",
                "temperatureInfluenceParams",
                "uncertainties"
            ],
            "title": "MeasurementProcessCharacteristic"
        },
        "TemperatureInfluenceParams": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "stringParam": {
                    "type": "null"
                },
                "numericalParam": {
                    "type": "integer"
                },
                "booleanParam": {
                    "type": "boolean"
                }
            },
            "required": [
                "booleanParam",
                "numericalParam",
                "stringParam"
            ],
            "title": "TemperatureInfluenceParams"
        },
        "Uncertainty": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {
                    "type": "string"
                },
                "value": {
                    "type": "integer"
                },
                "manualInput": {
                    "type": "boolean"
                },
                "active": {
                    "type": "boolean"
                },
                "notes": {
                    "type": "null"
                }
            },
            "required": [
                "active",
                "manualInput",
                "name",
                "notes",
                "value"
            ],
            "title": "Uncertainty"
        },
        "MeasurementSystem": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "code": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "characteristics": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/MeasurementSystemCharacteristic"
                    }
                },
                "masterObjects": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/MasterObject"
                    }
                },
                "uncertainties": {
                    "type": "null"
                }
            },
            "required": [
                "characteristics",
                "code",
                "masterObjects",
                "name",
                "uncertainties"
            ],
            "title": "MeasurementSystem"
        },
        "MeasurementSystemCharacteristic": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristicId": {
                    "type": "string"
                },
                "measurementMethod": {
                    "type": "string"
                },
                "measurementType": {
                    "type": "string"
                },
                "resolution": {
                    "type": "number"
                }
            },
            "required": [
                "characteristicId",
                "measurementMethod",
                "measurementType",
                "resolution"
            ],
            "title": "MeasurementSystemCharacteristic"
        },
        "MasterObject": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "masterObjectId": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "code": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "characteristicDimensions": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/CharacteristicDimension"
                    }
                },
                "calibrationDate": {
                    "type": "integer"
                },
                "note": {
                    "type": "null"
                }
            },
            "required": [
                "calibrationDate",
                "characteristicDimensions",
                "code",
                "masterObjectId",
                "name",
                "note",
                "type"
            ],
            "title": "MasterObject"
        },
        "CharacteristicDimension": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristicId": {
                    "type": "string"
                },
                "value": {
                    "type": "integer"
                }
            },
            "required": [
                "characteristicId",
                "value"
            ],
            "title": "CharacteristicDimension"
        },
        "MeasurementTask": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {
                    "type": "string"
                },
                "characteristics": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/MeasurementTaskCharacteristic"
                    }
                }
            },
            "required": [
                "characteristics",
                "name"
            ],
            "title": "MeasurementTask"
        },
        "MeasurementTaskCharacteristic": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "characteristicId": {
                    "type": "string"
                },
                "code": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "nominalValue": {
                    "type": "number"
                },
                "type": {
                    "type": "integer"
                },
                "unit": {
                    "type": "string"
                },
                "lowerSpecificationLimit": {
                    "$ref": "#/definitions/Limit"
                },
                "upperSpecificationLimit": {
                    "$ref": "#/definitions/Limit"
                },
                "lowerProcessLimit": {
                    "$ref": "#/definitions/Limit"
                },
                "upperProcessLimit": {
                    "$ref": "#/definitions/Limit"
                },
                "processCapabilityIndex": {
                    "type": "integer"
                }
            },
            "required": [
                "characteristicId",
                "code",
                "lowerProcessLimit",
                "lowerSpecificationLimit",
                "name",
                "nominalValue",
                "processCapabilityIndex",
                "type",
                "unit",
                "upperProcessLimit",
                "upperSpecificationLimit"
            ],
            "title": "MeasurementTaskCharacteristic"
        },
        "Limit": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "value": {
                    "type": "number"
                },
                "naturalBoundary": {
                    "type": "boolean"
                }
            },
            "required": [
                "naturalBoundary",
                "value"
            ],
            "title": "Limit"
        },
        "MasterObjectID": {
            "type": "string",
            "enum": [
                "7df64fda-3672-4bc4-b11d-3b9a50d5f90a",
                "8b976232-cb9e-4839-ab18-32939cf5a37b"
            ],
            "title": "MasterObjectID"
        }
    }
}
