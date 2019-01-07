FROM python:3

RUN pip install pika \
            && pip install requests \
            && pip install webthing

COPY ./senviro_webthing_broker.py .

CMD ["python", "-u", "senviro_webthing_broker.py"]
