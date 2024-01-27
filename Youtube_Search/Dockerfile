FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Youtube_Search.settings

RUN mkdir Youtube_Search
WORKDIR /Youtube_Search
COPY . /Youtube_Search

RUN pip install -r requirements.txt