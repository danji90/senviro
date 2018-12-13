from asyncio import sleep, CancelledError, get_event_loop
from webthing import (Action, Event, MultipleThings, Property, Thing, Value,
                      WebThingServer)
import logging
import random
import time
import uuid

# Actions

class tempShiftAction(Action):

    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'tempShift', input_=input_)

    def perform_action(self):
        self.thing.set_property('AirTemperature', self.input['AirTemperature'])


# Things classes
### TempHumidity sensor class
class tempHumSensor(Thing):

    def __init__(self):
        name = 'Si7021A20_humidityAndTemperature_sensor'
        type = ['AirTemperature', 'Humidity']
        description = "Monolithic CMOS IC integrating humidity and temperature sensor elements, an analog-to-digital converter, signal processing, calibration data, and an I2C Interface"
        Thing.__init__(self,
                       name,
                       type,
                       description)

        self.add_property(
            Property(self,
                     'AirTemperature',
                     Value(0, lambda v: print('Air temperature is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'AirTemperature',
                         'type': 'number',
                         'description': 'Real-Time air temperature reading in degrees Celsius',
                         'unit': 'degrees Celsius'
                     }))
        self.add_property(
            Property(self,
                     'Humidity',
                     Value(0, lambda v: print('Air humidity is now', v)),
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Humidity',
                         'type': 'number',
                         'description': 'Real-Time air humidity reading in %',
                         'minimum': 0,
                         'maximum': 100,
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




def run_server():
    # Create a thing that represents a dimmable light
    testSensor = tempHumSensor()

    # Create a thing that represents a humidity sensor
    # sensor = FakeGpioHumiditySensor()

    # If adding more than one thing, use MultipleThings() with a name.
    # In the single thing case, the thing's name will be broadcast.
    server = WebThingServer(MultipleThings([testSensor],
                                           'testDevice'),
                            port=8889)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.debug('canceling the sensor update looping task')
        sensor.cancel_update_level_task()
        logging.info('stopping the server')
        server.stop()
        logging.info('done')


if __name__ == '__main__':
    logging.basicConfig(
        level=10,
        format="%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s"
    )
run_server()
