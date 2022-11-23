FROM nvidia/cuda:11.3.1-devel-ubuntu20.04

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

RUN apt-get update && apt-get install -y --no-install-recommends \
  git vim wget curl build-essential unzip less \
  libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
  && curl https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tgz | tar zx \
  && cd Python-3.10.7 \
  && ./configure --enable-optimizations \
  && make -j$(nproc) \
  && make install \
  && ln -s $(which python3.10) /usr/bin/python \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/Python-3.10.7

RUN curl https://bootstrap.pypa.io/get-pip.py | python \
  && pip install ipython requests gdown \
  && pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 --extra-index-url https://download.pytorch.org/whl/cu113 \
  && pip cache purge

RUN git config --global credential.helper store

WORKDIR /app
