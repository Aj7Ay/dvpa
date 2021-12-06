FROM python:3.8-buster

COPY blog /app
WORKDIR /app
RUN apt update
RUN apt install -y default-libmysqlclient-dev gcc
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["/bin/bash", "-c", "python manage.py runserver"]