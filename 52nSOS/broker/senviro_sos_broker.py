import pika
import requests
import json
import sys
import ast
from datetime import datetime

# SOS baseUrl
baseUrl = "http://sos:8080/52n-sos-webapp/service"

with open('thingsSOS.json') as json_data:
    things = json.load(json_data)

with open('insertObservation.json') as json_data:
    observationTemplate = json.load(json_data)

uoms = {"AirTemperature":"°C","Humidity":"%","AtmosphericPressure":"Pa","Precipitation":"mm","WindDirection":"","WindSpeed":"m/s","SoilTemperature":"°C","SoilHumidity":"m^3/m^3","Battery":"%"}

connection = pika.BlockingConnection(pika.ConnectionParameters(host='senviro.init.uji.es', credentials=pika.credentials.PlainCredentials(username='senvmq', password='senviro.2018')))
channel = connection.channel()

channel.exchange_declare(exchange='amq.topic',
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

    # Create timestamp from message
    timestamp = str(datetime.strptime(str(body['time']), '%Y-%m-%d %H:%M:%S').isoformat())+"+00:00"

    # select correct thing from stations
    coordinates = list(filter(lambda x: x["id"] == str(nodeID), things))

    # Create observation object to post
    postObs = observationTemplate
    postObs["offering"] = "offering"+str(nodeID)
    postObs["observation"]["procedure"] = str(nodeID)
    postObs["observation"]["observedProperty"] = phenomenon
    postObs["observation"]["featureOfInterest"]["identifier"]["value"] = "featureOfInterest"+str(nodeID)
    postObs["observation"]["featureOfInterest"]["name"][0]["value"] = str(nodeID)
    postObs["observation"]["featureOfInterest"]["sampledFeature"] = ["parent"+str(nodeID)]                  # SampledFeature important for core operations
    postObs["observation"]["featureOfInterest"]["geometry"]["coordinates"] = coordinates[0]["location"]
    postObs["observation"]["phenomenonTime"] = timestamp
    postObs["observation"]["resultTime"] = timestamp
    postObs["observation"]["result"]["uom"] = uoms[str(phenomenon)]
    postObs["observation"]["result"]["value"] = float(body["value"])

    # Post object to service url
    # try:
    #     req = requests.post(baseUrl, json = postObs)
    #     req.raise_for_status()
    #
    #     print(req, "####", phenomenon, " observation for station " + nodeID + " inserted at " + str(datetime.now().isoformat()))
    # except:
    #     print(req, "####", "Could not insert observation at " + str(datetime.now().isoformat()))
    print(postObs)
def callback(ch, method, properties, body):

    # Extract thing unique name and observable property from message routing key
    thingName = str(method.routing_key).split('.')[2]
    obsPropName = str(method.routing_key).split('.')[3]

    # Decode byte message, throw error if decodification fails
    try:
        msg = ast.literal_eval(body.decode('utf-8'))
    except:
        print("Error: Message decodification failed, corrupted byte message (time: " + str(datetime.now().isoformat()) + ")")

    # Call insertObservation function, posts observations to sos db
    insertObservation(thingName, obsPropName, msg)

    # Message acknowledgement
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback, queue=queue_name)

channel.start_consuming()
