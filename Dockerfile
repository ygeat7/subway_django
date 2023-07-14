FROM python:3.9
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUBBERED 1

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
