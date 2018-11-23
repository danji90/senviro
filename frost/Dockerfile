FROM python:3

RUN pip install pika \
            && pip install requests

COPY ./broker.py .

CMD ["python", "-u", "broker.py", "#"]
