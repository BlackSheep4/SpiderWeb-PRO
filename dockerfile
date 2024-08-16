FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y sudo net-tools python3 wafw00f nmap whatweb git burpsuite gobuster openssl wfuzz  && \
    apt-get clean -y