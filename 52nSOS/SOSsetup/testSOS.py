import requests
import json
import sys
import ast
from datetime import datetime
import pytz
import tzlocal


procedure = {
  "swes:InsertSensor": {
    "-xmlns:gml": "http://www.opengis.net/gml/3.2",
    "-xmlns:sml": "http://www.opengis.net/sensorml/2.0",
    "-xmlns:sos": "http://www.opengis.net/sos/2.0",
    "-xmlns:swe": "http://www.opengis.net/swe/2.0",
    "-xmlns:swes": "http://www.opengis.net/swes/2.0",
    "-xmlns:xlink": "http://www.w3.org/1999/xlink",
    "-xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "-service": "SOS",
    "-version": "2.0.0",
    "-xsi:schemaLocation": "http://www.opengis.net/sos/2.0   http://schemas.opengis.net/swes/2.0/swes.xsd  http://schemas.opengis.net/sos/2.0/sosInsertSensor.xsd   http://www.opengis.net/swes/2.0   http://schemas.opengis.net/sensorML/2.0/sensorML.xsd  http://schemas.opengis.net/swes/2.0/swes.xsd",
    "swes:procedureDescriptionFormat": "http://www.opengis.net/sensorml/2.0",
    "swes:procedureDescription": {
      "sml:PhysicalSystem": {
        "-gml:id": "QuantumSensor_domef1500",
        "gml:identifier": {
          "-codeSpace": "uniqueID",
          "#text": "QuantumSensor_domef1500"
        },
        "sml:identification": {
          "sml:IdentifierList": {
            "sml:identifier": [
              {
                "sml:Term": {
                  "-definition": "urn:ogc:def:identifier:OGC:1.0:longName",
                  "sml:label": "longName",
                  "sml:value": "EURAC_GS_QuantumSensor_domef1500"
                }
              },
              {
                "sml:Term": {
                  "-definition": "urn:ogc:def:identifier:OGC:1.0:shortName",
                  "sml:label": "shortName",
                  "sml:value": "QuantumSensor_domef1500"
                }
              }
            ]
          }
        },
        "sml:capabilities": {
          "-name": "offerings",
          "sml:CapabilityList": {
            "sml:capability": {
              "-name": "offeringID",
              "swe:Text": {
                "-definition": "urn:ogc:def:identifier:OGC:offeringID",
                "swe:label": "PAR_domef1500",
                "swe:value": "PAR_domef1500"
              }
            }
          }
        },
        "sml:featuresOfInterest": {
          "sml:FeatureList": {
            "-definition": "http://www.opengis.net/def/featureOfInterest/identifier",
            "swe:label": "featuresOfInterest",
            "sml:feature": { "-xlink:href": "http://10.8.244.26:8080/52n-test/service/rest/sensors/QuantumSensor_domef1500" }
          }
        },
        "sml:inputs": {
          "sml:InputList": {
            "sml:input": {
              "-name": "Photosyntetcally_Active_Radiation",
              "sml:ObservableProperty": { "-definition": "Photosyntetcally_Active_Radiation" }
            }
          }
        },
        "sml:outputs": {
          "sml:OutputList": {
            "sml:output": [
              {
                "-name": "PARup_Avg",
                "swe:Category": {
                  "-definition": "Photosyntetcally_Active_Radiation_Up_Average",
                  "swe:codeSpace": { "-xlink:href": "NOT_DEFINED" }
                }
              },
              {
                "-name": "PARdn_Avg",
                "swe:Category": {
                  "-definition": "Photosyntetcally_Active_Radiation_Down_Average",
                  "swe:codeSpace": { "-xlink:href": "NOT_DEFINED" }
                }
              }
            ]
          }
        },
        "sml:position": {
          "swe:Vector": {
            "-referenceFrame": "urn:ogc:def:crs:EPSG::4326",
            "swe:coordinate": [
              {
                "-name": "easting",
                "swe:Quantity": {
                  "-axisID": "x",
                  "swe:uom": { "-code": "degree" },
                  "swe:value": "11.4542110"
                }
              },
              {
                "-name": "northing",
                "swe:Quantity": {
                  "-axisID": "y",
                  "swe:uom": { "-code": "degree" },
                  "swe:value": "46.4010020"
                }
              },
              {
                "-name": "altitude",
                "swe:Quantity": {
                  "-axisID": "z",
                  "swe:uom": { "-code": "m" },
                  "swe:value": "1415"
                }
              }
            ]
          }
        }
      }
    },
    "swes:observableProperty": [
      "PARup_Avg",
      "PARdn_Avg"
    ],
    "swes:metadata": {
      "sos:SosInsertionMetadata": {
        "sos:observationType": "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement",
        "sos:featureOfInterestType": "http://www.opengis.net/def/samplingFeatureType/OGC-OM/2.0/SF_SamplingPoint"
      }
    }
  }
}
