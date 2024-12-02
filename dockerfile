


FROM python:3.8-slim-buster as base 


ARG BUILD_ENV
ENV ENV_VAR ${BUILD_ENV}
WORKDIR /app


COPY . .

RUN pip3 install -r requirements.txt

RUN ls

RUN if [ "$ENV_VAR" = "dev" ]; then \
        echo 'dev' && \
        echo 'hi'; \
    elif [ "$ENV_VAR" = "prod" ]; then \
        gunicorn --bind 0.0.0.0:8080 app.py:Customer_API; \
    elif [ "$ENV_VAR" = "ci-testing" ]; then \
        pip install --upgrade pip && \
        pip install pytest; \
        pythoon3 app.py && \
        pytest tests/ ; \
        fi





#EXPOSE 5000

RUN python3 create_table.py
RUN ls

#RUN gunicorn --bind 0.0.0.0:8080 app.py:Customer_API