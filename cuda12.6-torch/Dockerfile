FROM --platform=linux/x86_64 nvcr.io/nvidia/cuda:12.6.3-cudnn-devel-ubuntu24.04

ARG PYTHON_VERSION=3.13
ARG PACKAGES="git curl ca-certificates vim wget unzip build-essential cmake jq gnupg"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_PROJECT_ENVIRONMENT="/usr/"

RUN apt-get update
RUN apt-get install -y --no-install-recommends ${PACKAGES}

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked <<INSTALL_UBUNTU_PYTHON
  fingerprint=F23C5A6CF475977595C89F51BA6932366A755776
  repo=deadsnakes
  subrepo=ppa
  ubuntu_version=$(. /etc/os-release && echo $VERSION_CODENAME)
  curl -sS "http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x${fingerprint}" > "./${repo}.asc"
  cat "./${repo}.asc" | gpg --dearmor -o "/etc/apt/keyrings/${repo}.gpg"
  echo "deb [signed-by=/etc/apt/keyrings/${repo}.gpg] http://ppa.launchpad.net/${repo}/${subrepo}/ubuntu ${ubuntu_version} main" | tee -a /etc/apt/sources.list.d/${repo}.list

  apt-get update
  apt-get install --no-install-recommends -y python${PYTHON_VERSION} python${PYTHON_VERSION}-dev
  ln -nfs /usr/bin/python${PYTHON_VERSION} /usr/bin/python
  ln -nfs /usr/bin/python${PYTHON_VERSION} /usr/bin/python3
  curl -sSL https://bootstrap.pypa.io/get-pip.py | python - --break-system-packages
  rm -rf /var/lib/apt/lists/*
  pip install uv
INSTALL_UBUNTU_PYTHON

RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126

WORKDIR /app
