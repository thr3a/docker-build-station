FROM --platform=linux/x86_64 nvcr.io/nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ARG PYTHON_VERSION=3.11
ARG PACKAGES="git curl ca-certificates vim wget unzip build-essential cmake jq"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv f23c5a6cf475977595c89f51ba6932366a755776 \
 && echo "deb http://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy main" > /etc/apt/sources.list.d/python.list \
 && echo "deb-src http://ppa.launchpad.net/deadsnakes/ppa/ubuntu jammy main" >> /etc/apt/sources.list.d/python.list

RUN apt-get update \
 && apt-get install -y --no-install-recommends ${PACKAGES} python${PYTHON_VERSION} \
 && ln -nfs /usr/bin/python${PYTHON_VERSION} /usr/bin/python \
 && ln -nfs /usr/bin/python${PYTHON_VERSION} /usr/bin/python3 \
 && rm -rf /var/lib/apt/lists/* \
 && curl -sSL https://bootstrap.pypa.io/get-pip.py | python -
RUN pip install torch==2.2.0 torchvision --index-url https://download.pytorch.org/whl/cu121

WORKDIR /app
