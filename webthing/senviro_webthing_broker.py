from asyncio import sleep, CancelledError, get_event_loop
from webthing import (Action, Event, MultipleThings, Property, Thing, Value,
                      WebThingServer)
# from multiprocessing import Process
import logging
import random
import time
import uuid
import threading
import sys
import pika
import requests
import json
import ast
from datetime import datetime

### WebThing setup
# Define Action class

class updateLocation(Action):
    # Allows users to update a node's coordinates
    def __init__(self, thing, input_):
        Action.__init__(self, uuid.uuid4().hex, thing, 'updateCoords', input_=input_)

    def perform_action(self):
        self.thing.set_property('Coordinates', self.input['Coordinates'])

# Define class for things (nodes) with properties and available actions
class senviroNode(Thing):

    def __init__(self, name, latlon):
        type = []
        description = "This monitoring station is an assemlby of sensors measuring environmental parameters in agricultural fields"
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
                         'unit': 'degree'
                     }))

        self.AirTemperature = Value(0.0)
        self.add_property(
            Property(self,
                     'AirTemperature',
                     self.AirTemperature,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'AirTemperature',
                         'type': 'number',
                         'description': 'The degree or intensity of heat present in the area',
                         'unit': 'degree celsius'
                     }))

        self.Humidity = Value(0.0)
        self.add_property(
            Property(self,
                     'Humidity',
                     self.Humidity,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Humidity',
                         'type': 'number',
                         'description': 'Ratio of the partial pressure of water vapor to the equilibrium vapor pressure of water at a given temperature',
                         'minimum': 0,
                         'maximum': 100,
                         'unit': 'percent'
                     }))

        self.AtmosphericPressure = Value(0.0)
        self.add_property(
            Property(self,
                     'AtmosphericPressure',
                     self.AtmosphericPressure,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'AtmosphericPressure',
                         'type': 'number',
                         'description': 'Pressure within the atmosphere of Earth',
                         'unit': 'pascal'
                     }))

        self.Precipitation = Value(0.0)
        self.add_property(
            Property(self,
                     'Precipitation',
                     self.Precipitation,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Precipitation',
                         'type': 'number',
                         'description': 'Product of the condensation of atmospheric water vapor that falls under gravity',
                         'unit': 'millimeters'
                     }))

        self.WindDirection = Value(0.0)
        self.add_property(
            Property(self,
                     'WindDirection',
                     self.WindDirection,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'WindDirection',
                         'type': 'number',
                         'description': 'Wind direction in integer values (0-7)',
                         'unit': 'null'
                     }))

        self.WindSpeed = Value(0.0)
        self.add_property(
            Property(self,
                     'WindSpeed',
                     self.WindSpeed,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'WindSpeed',
                         'type': 'number',
                         'description': 'Wind speed readings in m/s',
                         'unit': 'meters per second'
                     }))

        self.SoilTemperature = Value(0.0)
        self.add_property(
            Property(self,
                     'SoilTemperature',
                     self.SoilTemperature,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'SoilTemperature',
                         'type': 'number',
                         'description': 'The degree or intensity of heat present in the soil',
                         'unit': 'degrees celsius'
                     }))

        self.SoilHumidity = Value(0.0)
        self.add_property(
            Property(self,
                     'SoilHumidity',
                     self.SoilHumidity,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'SoilHumidity',
                         'type': 'number',
                         'description': 'Water content per soil ratio present in the soil',
                         'unit': 'm^3/m^3'
                     }))

        self.Battery = Value(0.0)
        self.add_property(
            Property(self,
                     'Battery',
                     self.Battery,
                     metadata={
                         '@type': 'LevelProperty',
                         'label': 'Battery',
                         'type': 'number',
                         'description': 'Battery readings in %',
                         'unit': 'percent'
                     }))

        self.add_available_action(
            'updateCoords',
            {
                'label': 'updateCoords',
                'description': 'Update station coordinates',
                'input': {
                    'type': 'object',
                    'required': [
                        'Coordinates'
                    ],
                    'properties': {
                        'Coordinates': {
                            'type': 'array',
                            'unit': 'degree'
                        },
                    },
                },
            },
            updateLocation)

# Create nodes for present stations, takes node ID and coordinates as arguments
node270043001951343334363036 = senviroNode("270043001951343334363036", [40.133098,-0.061000])
node4e0022000251353337353037 = senviroNode("4e0022000251353337353037", [39.993934,-0.073863])

### Rabbitmq configuration
def rabbitReceiver():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='senviro.init.uji.es', credentials=pika.credentials.PlainCredentials(username='senvmq', password='senviro.2018')))
    channel = connection.channel()
    channel.exchange_declare(exchange='amq.topic',
                             exchange_type='topic',
                             durable=True)

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    binding_keys = ['#']
    channel.queue_bind(exchange='amq.topic',
                           queue=queue_name,
                           routing_key=str(binding_keys[0]))

    print("Waiting for messages...")

    def callback(ch, method, properties, body):

        # Decode byte message, throw error if decodification fails
        try:
            msg = ast.literal_eval(body.decode('utf-8'))
        except:
            print("Error: Message decodification failed, corrupted byte message (time: " + str(datetime.now().isoformat()) + ")")

        thingName = str(method.routing_key).split('.')[2]
        obsPropName = str(method.routing_key).split('.')[3]

        node = globals()['node'+thingName]

        try:
            node.set_property(obsPropName, float(msg['value']))
            print("inserted: ", thingName, obsPropName, float(msg['value']))
        except:
            print("Could not insert ", obsPropName, " values for ", thingName,)


        ch.basic_ack(delivery_tag = method.delivery_tag)

        # return updateMsg(dummy)

    channel.basic_consume(callback, queue=queue_name)

    channel.start_consuming()

# Define RabbitMQ connection as simultaneous thread
mq_recieve_thread = threading.Thread(target=rabbitReceiver)

def run_server():

    # Define webthing server, add the two predefined nodes
    server = WebThingServer(MultipleThings([node270043001951343334363036, node4e0022000251353337353037],
                                           'senviroWeb'),
                            port=5000)
    # Start RabbitMQ thread
    mq_recieve_thread.start()

    try:
        # Start WebThing server
        print('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.debug('canceling the sensor update looping task')
        # node270043001951343334363036.cancel_update_level_task()
        print('stopping the server')
        server.stop()
        print('done')

# Run server
run_server()
