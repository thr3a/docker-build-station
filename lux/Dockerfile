FROM debian

WORKDIR /tmp

RUN apt-get update \
  && apt-get install -y --no-install-recommends ffmpeg curl ca-certificates \
  && curl -L https://github.com/iawia002/lux/releases/download/v0.19.0/lux_0.19.0_Linux_x86_64.tar.gz > lux.tar.gz \
  && tar xfv lux.tar.gz \
  && mv lux /usr/local/bin/lux \
  && rm -f lux.tar.gz \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["lux"]
