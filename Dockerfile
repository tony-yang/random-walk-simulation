FROM ubuntu
RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    tcl \
 && ln -s /usr/bin/python3 /usr/bin/python \
 && pip3 install --upgrade \
    pip

WORKDIR /root

ADD . /root/
