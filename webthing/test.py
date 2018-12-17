from asyncio import sleep, CancelledError, get_event_loop
from webthing import (Action, Event, MultipleThings, Property, Thing, Value,
                      WebThingServer)
import logging
import random
import time
import uuid
import sys
import pika
import requests
import json
import ast
from datetime import datetime

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

        # Extract message properties from message
        thingName = str(method.routing_key).split('.')[2]
        obsPropName = str(method.routing_key).split('.')[3]
        date = datetime.strptime(str(msg['time']), '%Y-%m-%d %H:%M:%S')
        result = float(msg['value'])

        msgFull = {"thing":thingName,"phenomenon":obsPropName,"date":str(date.isoformat()),"result":result}

        # Message acknowledgement
        ch.basic_ack(delivery_tag = method.delivery_tag)

        print(msgFull)

    channel.basic_consume(callback, queue=queue_name)

    channel.start_consuming()

rabbitReceiver()
