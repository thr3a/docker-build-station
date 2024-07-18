FROM ubuntu:14.04

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential wget m4 git \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# OCamlのインストール
RUN wget http://caml.inria.fr/pub/distrib/ocaml-3.09/ocaml-3.09.3.tar.gz \
  && tar zxvf ocaml-3.09.3.tar.gz \
  && cd ocaml-3.09.3 \
  && ./configure \
  && make world.opt \
  && make install

# Findlibのインストール
RUN wget http://download.camlcity.org/download/findlib-1.2.1.tar.gz \
  && tar zxvf findlib-1.2.1.tar.gz \
  && cd findlib-1.2.1 \
  && ./configure \
  && make all \
  && make opt \
  && make install

# OMakeのインストール
RUN wget http://web.archive.org/web/20070623190729/mojave.metaprl.org/download/omake/omake-0.9.6.8-1.tar.gz \
  && tar zxvf omake-0.9.6.8-1.tar.gz \
  && cd omake-0.9.6.8 \
  && make install

# ExtLibのインストール
COPY prompt.txt /app/extlib-1.4/prompt.txt
RUN wget -O extlib-1.4.tgz https://sourceforge.net/projects/ocaml-lib/files/extlib/extlib-1.4/extlib-1.4.tgz/download \
  && tar zxvf extlib-1.4.tgz \
  && cd extlib-1.4 \
  && ocaml install.ml < prompt.txt

# Ulexのインストール
RUN wget http://www.cduce.org/download/old/ulex-0.8.tar.gz \
  && tar zxvf ulex-0.8.tar.gz \
  && cd ulex-0.8 \
  && make all.opt \
  && make install

# RLDevのビルド
RUN git clone --depth 1 https://github.com/eglaysher/rldev.git \
  && cd rldev/src \
  && ./configure \
  && omake \
  && omake install
