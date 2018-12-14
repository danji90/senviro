from asyncio import sleep, CancelledError, get_event_loop
from webthing import (Action, Event, MultipleThings, Property, Thing, Value,
                      WebThingServer)
import logging
import random
import time
import uuid
import sys

# Actions
class tempShiftEvent(Event):

    def __init__(self, thing, data, input_):
        Event.__init__(self, thing, 'tempChange', data=data)
        self.thing.set_property('AirTemperature', self.input['AirTemperature'])


class tempShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'tempShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('AirTemperature', self.input['AirTemperature'])

class humShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'humShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('Humidity', self.input['Humidity'])

class pressureShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'pressureShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('AtmosphericPressure', self.input['AtmosphericPressure'])

class precShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'precShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('Precipitation', self.input['Precipitation'])

class windDirShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'windDirShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('WindDirection', self.input['WindDirection'])

class windSpeedShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'windSpeedShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('WindSpeed', self.input['WindSpeed'])

class soilTempShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'soilTempShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('SoilTemperature', self.input['SoilTemperature'])

class soilHumShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'soilHumShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('SoilHumidity', self.input['SoilHumidity'])

class batteryShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'batteryShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('Battery', self.input['Battery'])

# Things classes
### TempHumidity sensor class
class senviroNode(Thing):

    def __init__(self, name, latlon):
        # name = "SenviroNode"
        type = []
        # description = "Monolithic CMOS IC integrating humidity and temperature sensor elements, an analog-to-digital converter, signal processing, calibration data, and an I2C Interface"
        description = "This monitoring station is an assemlby of sensors measuring environmental parameters in agricultural fields"
        # coordinates = []
        Thing.__init__(self,
                       name,
                       type,
                       description)

        self.add_property(
            Property(self,
                     'Coordinates',
                     Value(latlon),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Coordinates',
                         'type': 'array',
                         'description': 'Latitude and longitude coordinates of the station',
                         'unit': 'degree',
                         'readOnly': True
                     }))

        self.add_property(
            Property(self,
                     'AirTemperature',
                     Value(0, lambda v: print('Air temperature is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'AirTemperature',
                         'type': 'number',
                         'description': 'The degree or intensity of heat present in the area',
                         'unit': 'degree celsius'
                     }))

        self.add_property(
            Property(self,
                     'Humidity',
                     Value(0, lambda v: print('Air humidity is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Humidity',
                         'type': 'number',
                         'description': 'Ratio of the partial pressure of water vapor to the equilibrium vapor pressure of water at a given temperature',
                         'minimum': 0,
                         'maximum': 100,
                         'unit': 'percent'
                     }))

        self.add_property(
            Property(self,
                     'AtmosphericPressure',
                     Value(0, lambda v: print('Pressure is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'AtmosphericPressure',
                         'type': 'number',
                         'description': 'Pressure within the atmosphere of Earth',
                         'unit': 'pascal'
                     }))

        self.add_property(
            Property(self,
                     'Precipitation',
                     Value(0, lambda v: print('Precipitation is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Precipitation',
                         'type': 'number',
                         'description': 'Product of the condensation of atmospheric water vapor that falls under gravity',
                         'unit': 'millimeters'
                     }))

        self.add_property(
            Property(self,
                     'WindDirection',
                     Value(0, lambda v: print('Wind direction is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'WindDirection',
                         'type': 'integer',
                         'description': 'Wind direction in integer values (0-7)',
                         'unit': 'null'
                     }))

        self.add_property(
            Property(self,
                     'WindSpeed',
                     Value(0, lambda v: print('Wind speed is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'WindSpeed',
                         'type': 'number',
                         'description': 'Wind speed readings in m/s',
                         'unit': 'meters per second'
                     }))

        self.add_property(
            Property(self,
                     'SoilTemperature',
                     Value(0, lambda v: print('Soil temperature is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'SoilTemperature',
                         'type': 'number',
                         'description': 'The degree or intensity of heat present in the soil',
                         'unit': 'degrees celsius'
                     }))

        self.add_property(
            Property(self,
                     'SoilHumidity',
                     Value(0, lambda v: print('Soil humidity is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'SoilHumidity',
                         'type': 'number',
                         'description': 'Water content per soil ratio present in the soil',
                         'unit': 'm^3/m^3'
                     }))

        self.add_property(
            Property(self,
                     'Battery',
                     Value(0, lambda v: print('Battery percentage is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Battery',
                         'type': 'number',
                         'description': 'Battery readings in %',
                         'unit': 'percent'
                     }))

        self.add_available_action(
            'tempShift',
            {
                'label': 'tempShift',
                'description': 'Temperature change',
                'input': {
                    'type': 'object',
                    'required': [
                        'AirTemperature'
                    ],
                    'properties': {
                        'AirTemperature': {
                            'type': 'number',
                            'unit': 'degrees Celsius',
                        },
                    },
                },
            },
            tempShiftAction)

        self.add_available_action(
            'humShift',
            {
                'label': 'humShift',
                'description': 'Humidity change',
                'input': {
                    'type': 'object',
                    'required': [
                        'Humidity'
                    ],
                    'properties': {
                        'Humidity': {
                            'type': 'number',
                            'unit': 'percent',
                        },
                    },
                },
            },
            humShiftAction)

        self.add_available_action(
            'pressureShift',
            {
                'label': 'humShift',
                'description': 'Atmospheric Pressure change',
                'input': {
                    'type': 'object',
                    'required': [
                        'AtmosphericPressure'
                    ],
                    'properties': {
                        'AtmosphericPressure': {
                            'type': 'number',
                            'unit': 'pascal',
                        },
                    },
                },
            },
            pressureShiftAction)

        self.add_available_action(
            'precShift',
            {
                'label': 'humShift',
                'description': 'Precipitation change',
                'input': {
                    'type': 'object',
                    'required': [
                        'Precipitation'
                    ],
                    'properties': {
                        'Precipitation': {
                            'type': 'number',
                            'unit': 'millimeters',
                        },
                    },
                },
            },
            precShiftAction)

        self.add_available_action(
            'windDirShift',
            {
                'label': 'humShift',
                'description': 'Wind direction change',
                'input': {
                    'type': 'object',
                    'required': [
                        'WindDirection'
                    ],
                    'properties': {
                        'WindDirection': {
                            'type': 'intger',
                            'unit': 'null',
                        },
                    },
                },
            },
            windDirShiftAction)

        self.add_available_action(
            'windSpeedShift',
            {
                'label': 'windSpeedShift',
                'description': 'Wind speed change',
                'input': {
                    'type': 'object',
                    'required': [
                        'WindSpeed'
                    ],
                    'properties': {
                        'WindSpeed': {
                            'type': 'number',
                            'unit': 'meters per second',
                        },
                    },
                },
            },
            windSpeedShiftAction)

        self.add_available_action(
            'soilTempShift',
            {
                'label': 'soilTempShift',
                'description': 'Soil temperature change',
                'input': {
                    'type': 'object',
                    'required': [
                        'SoilTemperature'
                    ],
                    'properties': {
                        'SoilTemperature': {
                            'type': 'number',
                            'unit': 'degrees celsius',
                        },
                    },
                },
            },
            soilTempShiftAction)

        self.add_available_action(
            'soilHumShift',
            {
                'label': 'soilHumShift',
                'description': 'Soil humidity change',
                'input': {
                    'type': 'object',
                    'required': [
                        'SoilHumidity'
                    ],
                    'properties': {
                        'SoilHumidity': {
                            'type': 'number',
                            'unit': 'percent',
                        },
                    },
                },
            },
            soilHumShiftAction)

        self.add_available_action(
            'batteryShift',
            {
                'label': 'batteryShift',
                'description': 'Battery percentage change',
                'input': {
                    'type': 'object',
                    'required': [
                        'Battery'
                    ],
                    'properties': {
                        'Battery': {
                            'type': 'number',
                            'unit': 'percent',
                        },
                    },
                },
            },
            batteryShiftAction)

        self.add_available_event(
            'tempChange',
            {
                'description':
                'The lamp has exceeded its safe operating temperature',
                'type': 'number',
                'unit': 'degree celsius',
                })

# def createNode(nodeId, latLon):
#     node = senviroNode()
#     node.name = nodeId
#     node.href = "/"+nodeId
#     node.type = latLon
#     return node



def run_server():
    # Create a thing that represents a dimmable light

    node270043001951343334363036 = senviroNode("270043001951343334363036", [40.141384,-0.026397])
    node4e0022000251353337353037 = senviroNode("4e0022000251353337353037", [40.133098,-0.061])

    node270043001951343334363036.add_event(tempShiftEvent(node270043001951343334363036, {"time":"11/11/2018 13:12.34", "value":1234}, 1234))

    # Create a thing that represents a humidity sensor
    # sensor = FakeGpioHumiditySensor()
    # print(node270043001951343334363036.href)
    # If adding more than one thing, use MultipleThings() with a name.
    # In the single thing case, the thing's name will be broadcast.
    server = WebThingServer(MultipleThings([node270043001951343334363036, node4e0022000251353337353037],
                                           'senviroWeb'),
                            port=8889)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.debug('canceling the sensor update looping task')
        # sensor.cancel_update_level_task()
        logging.info('stopping the server')
        server.stop()
        logging.info('done')

if __name__ == '__main__':
    logging.basicConfig(
        level=10,
        format="%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s"
    )

run_server()
