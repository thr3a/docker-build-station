FROM python:3-slim

ENV TZ=Asia/Tokyo
ENV PIP_NO_CACHE_DIR=on

RUN apt-get update \
  && apt-get install -y --no-install-recommends git \
  && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/frozenpandaman/s3s \
  && pip install -r /s3s/requirements.txt

WORKDIR /s3s
