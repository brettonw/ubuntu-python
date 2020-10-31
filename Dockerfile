FROM ubuntu:bionic

RUN apt-get update && apt-get -yq install python3 python3-distutils python3-pip linux-headers-generic nano curl nmap zip;
RUN ln -s /usr/bin/python3 /usr/bin/python;
RUN pip3 install python-nmap pynput;



