FROM python:3.8-slim-buster

WORKDIR /app


COPY . .

RUN pip3 install -r requirements.txt


#EXPOSE 5000

RUN python3 create_table.py


#RUN gunicorn --bind 0.0.0.0:8080 app.py:Customer_API