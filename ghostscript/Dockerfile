FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends ghostscript \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["gs"]
