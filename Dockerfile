FROM python:slim

# install basic utilities
RUN \
  apt-get -qq -y update && \
  apt-get -qq -y upgrade && \
  apt-get install -y jq git tree hdf5-tools bash-completion && \
  apt-get clean && \
  rm -rf /var/lib/apt-get/lists/* && \
  true

# python installs
COPY requirements.txt .
RUN \
  pip3 install --upgrade pip && \
  pip3 install -r requirements.txt

CMD /bin/bash
