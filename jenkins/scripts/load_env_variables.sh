#!/usr/bin/env bash

load_variables() {
  cd $WORKSPACE
  echo SLACK_TOKEN=$SLACK_TOKEN > .env
  echo ENV=$ENV >> .env
  echo DEBUG=$DEBUG >> .env
  echo PORT=$PORT >> .env
  echo SECRET_KEY=$SECRET_KEY >> .env
  echo MONGO_URL=$MONGO_URL >> .env
  echo HOST=$HOST >> .env

  export $(cat .env)
}

main() {
  load_variables
}

main
