

FROM python:3.8-slim-buster AS base 

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM base AS test
RUN pip3 install pytest
ENTRYPOINT pytest tests/


FROM base AS development


FROM base AS production 
