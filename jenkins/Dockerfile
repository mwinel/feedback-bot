FROM python:3.6.9-stretch

USER root

ENV PATH=$PATH:/usr/local/gcloud/google-cloud-sdk/bin

RUN apt-get update && apt-get install bash curl tar && \
  pip3 install virtualenv

RUN wget --quiet https://releases.hashicorp.com/terraform/0.11.10/terraform_0.11.10_linux_amd64.zip \
  && unzip terraform_0.11.10_linux_amd64.zip \
  && mv terraform /usr/local/bin \
  && rm terraform_0.11.10_linux_amd64.zip

RUN curl -sSL https://get.docker.com/ | bash && \
   curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-245.0.0-linux-x86_64.tar.gz && \
    tar zxvf google-cloud-sdk-245.0.0-linux-x86_64.tar.gz google-cloud-sdk && \
    ./google-cloud-sdk/install.sh && \
    rm google-cloud-sdk-245.0.0-linux-x86_64.tar.gz && \
    mkdir -p /usr/local/gcloud && \
    mv google-cloud-sdk /usr/local/gcloud && \
    gcloud components install kubectl && \
    echo n | gcloud init
