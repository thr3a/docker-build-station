FROM ubuntu:latest

ENV TZ=Asia/Tokyo
ENV FFMPEG_VERSION=6.0

WORKDIR /tmp

# RUN apt-get -y update && \
#   apt-get install -y --no-install-recommends build-essential cmake pkg-config git && \
#   rm -rf /var/lib/apt/lists/*

RUN apt-get -y update
WORKDIR /app

# ENTRYPOINT ["ffmpeg"]


## Download ffmpeg https://ffmpeg.org/
RUN DIR=/tmp/ffmpeg && mkdir -p ${DIR} && cd ${DIR} && \
  wget https://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.bz2 && \
  tar -jx --strip-components=1 -f ffmpeg-${FFMPEG_VERSION}.tar.bz2 && \
  ./configure --disable-debug --disable-doc --disable-ffplay --enable-shared --enable-gpl --extra-libs=-ldl && \
  make -j && make install
