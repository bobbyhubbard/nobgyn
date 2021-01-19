FROM python:3.8.3-alpine

ENV APP_NAME=/home/app/northlandobgyn
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory


RUN mkdir -p $APP_NAME
RUN mkdir -p $APP_NAME_static

# where the code lives
WORKDIR $APP_NAME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $APP_NAME
RUN pip install -r requirements.txt
COPY ./entrypoint.sh $APP_NAME

CMD ["/bin/bash", "/home/app/microservice/entrypoint.sh"]
