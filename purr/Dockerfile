# Dockerfile
FROM python:3.11.2-slim-bullseye

WORKDIR /purr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .


CMD ["python3", "mqtt_to_mongodb.py"]