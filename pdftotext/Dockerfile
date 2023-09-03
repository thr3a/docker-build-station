FROM ubuntu:devel

RUN apt-get update \
  && apt-get install -y --no-install-recommends poppler-utils \
  && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/bin/pdftotext"]

CMD ["-layout", "-", "-"]
