FROM python:3.8.1

ENV PYTHONUNBUFFERED 1

MAINTAINER Nosach Mykola

RUN mkdir /src

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src/