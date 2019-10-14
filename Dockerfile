FROM python:slim

# install basic utilities
RUN \
  apt-get -qq -y update && \
  apt-get -qq -y upgrade && \
  apt-get install -y jq git tree hdf5-tools bash-completion && \
  apt-get install -y ffmpeg vim emacs&& \
  apt-get clean && \
  rm -rf /var/lib/apt-get/lists/* && \
  true

# add repository to the image

# python installs
COPY requirements.txt .
RUN \
  pip3 install --upgrade pip && \
  pip3 install -r requirements.txt

RUN useradd -m grk
COPY . /home/grk
RUN chown -R grk:grk /home/grk
USER grk
WORKDIR /home/grk

CMD /bin/bash
