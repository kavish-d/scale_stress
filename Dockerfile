FROM python:3.8.3

ENV C_FORCE_ROOT 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /pydash

WORKDIR  /pydash

ADD . /pydash/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
