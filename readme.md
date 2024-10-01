# Customer API



# Getting Started

buidl container 
`
docker build -t passenger_mock .

`


run container 

`
docker run -it passenger_mock

`


Run Gunicorn with 

gunicorn --bind 0.0.0.0:8080