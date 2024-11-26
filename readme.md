# Customer API
This is a customer API i built to use for testing different patterns or solutions. I am utlizing self hosted github runners on a raspberry pi. This rspberry pi is being used to host the the flask Customer APi.


# Getting Started
The following software is required to get started. I am using docker to do development and for usage on my raspberry pi. The raspberry pi 3b+ is running on my home network. I currently have a self hosted runner from github running when making commits to the main branch. 



## Local Development Workflow
I have been running the following commands in docker to build the container. 
`
docker build -t passenger_mock .

`

The following command is what I am using to run the docker container in interactive mode. 
run container 

`
docker run -it passenger_mock

`
