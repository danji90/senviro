import pika
import requests
import json
import sys

# FROST-Server baseUrl
baseUrl = "http://elcano.init.uji.es:8082/FROST-Server/v1.0"

# SensorThings API classes
staClass = ["Datastreams", "MultiDatastreams", "FeaturesOfInterest", "HistoricalLocations", "Locations", "Observations", "ObservedProperties", "Sensors", "Things"]

connection = pika.BlockingConnection(pika.ConnectionParameters(host='senviro.init.uji.es', credentials=pika.credentials.PlainCredentials(username='senvmq', password='senviro.2018')))
channel = connection.channel()

channel.exchange_declare(exchange='amq.topic',    # amq.topic
                         exchange_type='topic',
                         durable=True)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='amq.topic',
                       queue=queue_name,
                       routing_key=binding_key)


print(' [*] Waiting for logs. To exit press CTRL+C')

def thingHandler():
    things = requests.get(baseUrl + '/' + 'Things').json()


def obsPropHandler(messagePropString):
    obsProp = requests.get(baseUrl + '/' + 'ObservedProperties').json()
    if obsProp['value'] == []:
        requests.post(baseUrl + '/' + 'ObservedProperties', json = {"name": messagePropString, "description": "", "definition": ""})
        print(messagePropString)
    else:
        props = []
        for prop in obsProp['value']:
            props.append(prop['name'])

        if messagePropString not in props:
            requests.post(baseUrl + '/' + 'ObservedProperties', json = {"name": messagePropString, "description": "", "definition": ""})

def callback(ch, method, properties, body):

    rest, thingName, obsPropName = str(method.routing_key).rsplit('.', 2)

    obsPropHandler(obsPropName)

    print(" [x] %r:%r" % (method.routing_key, body))
    print("obsPropName: ", obsPropName)

#
#     # add this for Senviro for message acknowledgement
#     # def callback(ch, method, properties, body):
#     # print " [x] Received %r" % (body,)
#     # time.sleep( body.count('.') )
#     # print " [x] Done"
#     # ch.basic_ack(delivery_tag = method.delivery_tag)
#
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)                  #   delete no_ack or set to false in senviro

channel.start_consuming()
