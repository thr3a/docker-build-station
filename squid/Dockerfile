FROM ubuntu:24.04

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y squid && \
    rm -rf /var/lib/apt/lists/*

COPY docker.conf /etc/squid/conf.d/

CMD ["/usr/sbin/squid", "-N"]
