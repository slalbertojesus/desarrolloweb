FROM python:3.7.0

ENV PYTHONNUNBUFFERED 1 

RUN mkdir /Proyecto

WORKDIR /Proyecto

COPY requirements.txt /Proyecto/

RUN pip --no-cache-dir install --upgrade -r requirements.txt

COPY . /Proyecto/ 
