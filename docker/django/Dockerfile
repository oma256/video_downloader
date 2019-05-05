FROM python:3.7
MAINTAINER  Dulatov Omurbek <oma.dulatov@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .

EXPOSE 3000