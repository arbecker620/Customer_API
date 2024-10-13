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