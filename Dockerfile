FROM python:3.9.6-alpine

# set work directory
WORKDIR ./

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN pip install ruamel.yaml
RUN pip install ruamel.yaml.jinja2

#COPY ./entrypoint.sh .

ENV HOME=/home/RishadTEst/
ENV APP_HOME=/home/RishadTEst/
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles/
RUN mkdir $APP_HOME/media/
WORKDIR $APP_HOME

COPY . .
