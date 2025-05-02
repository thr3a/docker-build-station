FROM --platform=linux/x86_64 python:3.11-slim

ARG PACKAGES="git curl ca-certificates vim wget unzip build-essential cmake jq"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_PROJECT_ENVIRONMENT="/usr/"

RUN apt-get update && apt-get install -y --no-install-recommends ${PACKAGES}

RUN pip install -U pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install uv

WORKDIR /app
