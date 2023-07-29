FROM python:alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir flask flask-api ifaddr


ENV FLASK_APP src

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && pip install -r requirements.txt \
    && apk del build-deps


COPY . .


CMD ["flask", "run"]