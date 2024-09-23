FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on
ENV PYTHONDONTWRITEBYTECODE=1

RUN python3 -m pip install PyGithub

ADD main.py /

WORKDIR /app
ENTRYPOINT ["python3", "/main.py"]
