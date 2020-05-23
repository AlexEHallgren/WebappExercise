FROM python:3.8.3-alpine

LABEL maintainer="Alexander Hallgren alex.ehallgren@gmail.com"

RUN apk update && apk add bash

COPY requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

COPY /app /app

ENTRYPOINT [ "python" ]
CMD [ "app/app.py" ]

