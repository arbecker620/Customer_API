# Customer API
This is a customer API i built to use for testing different patterns or solutions. I am hosting some self hoster github runners on a raspberry pi. This rspberry pi is being used to host the the flask Customer APi.


# Getting Started
The following software is required to get started. I am using docker to do development and for usage on my raspberry pi. The raspberry pi 3b+ is running on my home network. 


I have been running the following commands in docker to build the container 
`
docker build -t passenger_mock .

`

The following command is whjat I am using to run the docker container in interactive mode. 
run container 

`
docker run -it passenger_mock

`


Run Gunicorn with 

gunicorn --bind 0.0.0.0:8080


  deploy:
    runs-on: self-hosted
    needs: build
    
    steps:
      # Kill gunicorn server, if running already
      - name: Kill gunicorn
        run: pkill gunicorn || true

      # Run gunicorn server
      - name: Run gunicorn
        run: |
          source flask-env/bin/activate
          RUNNER_TRACKING_ID=""
          gunicorn -w 1 -b 0.0.0.0:4000 app:app -D --log-file=gunicorn.log