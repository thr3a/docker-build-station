FROM ubuntu:24.04

RUN apt-get update \
  && apt-get install -y --no-install-recommends ffmpeg curl ca-certificates \
  && rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/Based-Programmer/titans/releases/download/v4.0.7/titans > /usr/local/bin/titan

# ENTRYPOINT ["/usr/bin/pdftotext"]

# CMD ["-layout", "-", "-"]
