# Example

Here are some example queries for the sensorThings API:


- Get all observations of all properties of a specific thing

http://elcano.init.uji.es:8082/FROST-Server/v1.0/Things(1)?$expand=Datastreams($expand=Observations)


- Get all observations of all properties of a specific thing within a specified time window (doesn't work):

http://elcano.init.uji.es:8082/FROST-Server/v1.0/Things(1)?$expand=Datastreams($expand=Observations)&$filter=Datastreams/Observations/phenomenonTime%20ge%202018-11-28T00:45:45.842Z%20and%20Datastreams/Observations/phenomenonTime%20le%202019-01-10T05:02:05.445Z


- Get observations within a specified time interval from one datastream:

http://elcano.init.uji.es:8082/FROST-Server/v1.0/Datastreams(1)/Observations?$select=phenomenonTime,result&$filter=phenomenonTime%20gt%202018-11-28T00:45:45.842Z%20and%20phenomenonTime%20lt%202019-01-10T05:02:05.445Z