FROM python:3.6.9-stretch

WORKDIR /app

COPY . /app

RUN pip3 install python-dotenv && \
  export $(cat .env) && \
  pip3 install -r requirements.txt

EXPOSE 5500

CMD [ "python3", "app.py", "run_server" ]
