#!/usr/bin/env bash

source $WORKSPACE/jenkins/scripts/utils.sh

# authenticate to GCR
auth_to_docker_registry() {
  info "Authenticating to GCR"
  if [ "$GIT_BRANCH" == master ] || [ "$GIT_BRANCH" == develop ]; then
    docker login -u _json_key -p "$(echo $GOOGLE_CREDENTIALS_PRODUCTION | base64 --decode)" https://gcr.io
  else
    docker login -u _json_key -p "$(echo $GOOGLE_CREDENTIALS_PRODUCTION | base64 --decode)" https://gcr.io
  fi
  success "Authentication successful"
}

#  Updating the image version to the latest
save_image_version() {
  info "Updating the image version to the latest"
  if [ "$GIT_BRANCH" == master ]; then
    # update slack_microservice production image version on GCR
    gsutil cp current_version gs://${PRODUCTION_SLACK_MICROSERVICE_IMAGE_VERSION_PATH}
  else
    gsutil cp current_version gs://${STAGING_SLACK_MICROSERVICE_IMAGE_VERSION_PATH}
  fi
  success "Image version updated successfully"
}

# build and push image
build_docker_image() {
  info "Building docker image"
  if [ "$GIT_BRANCH" == master ]; then
    # build docker image and tag it with production slack_microservice image name
    docker build $WORKSPACE/Dockerfile -t ${PRODUCTION_SLACK_MICROSERVICE_IMAGE}:${IMAGE_TAG} .
    success "Docker Image built successfully"
    # push image to production slack_microservice image path
    docker push ${PRODUCTION_SLACK_MICROSERVICE_IMAGE}:${IMAGE_TAG}
  else
    # build docker image and tag it with production slack_microservice image name
    docker build -f $WORKSPACE/Dockerfile -t ${STAGING_SLACK_MICROSERVICE_IMAGE}:${IMAGE_TAG} .
    success "Docker Image built successfully"
    # push image to production slack_microservice image path
    docker push ${STAGING_SLACK_MICROSERVICE_IMAGE}:${IMAGE_TAG}
  fi
  success "Docker Image successfully pushed to container registry"
}


run_build() {
  export PATH=$PATH:/usr/local/gcloud/google-cloud-sdk/bin
  cd $WORKSPACE
  auth_to_docker_registry
  build_docker_image
  touch current_version
  echo ${IMAGE_TAG} > current_version
  save_image_version
}

main() {
  run_build
}

main
