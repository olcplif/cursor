FROM python:3.9-slim

RUN apt-get update && apt-get install -y gettext

ADD . /restaurant

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /restaurant/requirements/dev.txt

WORKDIR restaurant/src