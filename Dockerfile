FROM python:3.6.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /Proyecto

WORKDIR /Proyecto

COPY requirements.txt /Proyecto/

RUN pip --no-cache-dir install --upgrade -r requirements.txt

COPY . /Proyecto/ 
