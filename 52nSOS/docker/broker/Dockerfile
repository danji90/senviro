FROM python:3

RUN pip install pika \
            && pip install requests

			
COPY ./senviro_sos_broker.py .
COPY ./insertObservation.json .
COPY ./thingsSOS.json .

CMD ["python", "-u", "senviro_sos_broker.py", "#"]
