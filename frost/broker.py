import pika
import requests
import json
import sys
import ast

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

def insertObservation(nodeID, phenomenon, body):

    # Datastreams base url
    url = baseUrl + '/' + 'Datastreams'

    # Load name and id of present datastreams
    dataStreams = requests.get(url + '?$select=name,id').json()

    # Empty variable for holding the target datastream id
    sendingDatastreamID = None

    # Get correct datastream id using the routing key parameters of the message, save it in variable
    for stream in dataStreams['value']:
        if stream['name'] == phenomenon+'-'+nodeID:
            sendingDatastreamID = stream['@iot.id']

    # Create observation object to post
    postObs = {"resultTime" :  body['time'].replace(" ","T"),"result" : float(body['value'])}

    # Post object to datastreams(id)/observations
    try:
        req = requests.post(url + '(' + str(sendingDatastreamID) + ')' + '/' + 'Observations', json = postObs)
        req.raise_for_status()
        print(req, "####", phenomenon, " observation for station " + nodeID + " inserted")
    except:
        print(req, "####", "Could not insert observation" )


def callback(ch, method, properties, body):

    # Estract thing unique name and observable property from message routing key
    thingName = str(method.routing_key).split('.')[2]
    obsPropName = str(method.routing_key).split('.')[3]

    # Decode byte message
    msg = ast.literal_eval(body.decode('utf-8'))

    # Call insertObservation function, posts observations to frost db
    insertObservation(thingName, obsPropName, msg)
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
