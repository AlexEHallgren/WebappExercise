FROM python:3.8.3-alpine

LABEL maintainer="Alexander Hallgren alex.ehallgren@gmail.com"

COPY requirements.txt /exercise/
WORKDIR /exercise

RUN pip install -r requirements.txt

COPY app app

ENTRYPOINT [ "python" ]
CMD [ "app/manage.py", "runserver", "0.0.0.0:8000" ]

