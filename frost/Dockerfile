FROM python:3

RUN pip install pika \
            && pip install requests

COPY ./senviro_frost_broker.py .

CMD ["python", "-u", "senviro_frost_broker.py", "#"]
