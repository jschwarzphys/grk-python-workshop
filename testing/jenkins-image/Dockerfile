FROM jenkins/jenkins:lts
USER root
RUN apt-get update \
    && apt-get install -y python3-pip python3 \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install -U pytest tox
USER jenkins
