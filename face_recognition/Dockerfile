FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_CACHE_DIR=off
ENV TZ=Asia/Tokyo

WORKDIR /tmp

RUN apt-get -y update && \
  apt-get install -y --no-install-recommends build-essential cmake pkg-config && \
  rm -rf /var/lib/apt/lists/*

RUN pip install opencv-python-headless==4.7.0.68 dlib==19.24.0

WORKDIR /app

ADD index.py /

ENTRYPOINT ["python", "/index.py"]
