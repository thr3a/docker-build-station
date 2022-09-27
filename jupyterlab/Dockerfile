FROM jupyter/tensorflow-notebook:latest

ENV TZ=Asia/Tokyo
ENV JUPYTER_TOKEN=pass

USER root

WORKDIR /tmp
RUN apt-get update \
  && apt-get install -y --no-install-recommends mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 file build-essential curl \
  && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
  && mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y \
  && cp /etc/mecabrc /usr/local/etc/ \
  && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --quiet --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN mkdir -p /home/${NB_USER}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/ \
    && mkdir -p /home/${NB_USER}/.jupyter/lab/user-settings/@jupyterlab/terminal-extension/

COPY themes.jupyterlab-settings /home/${NB_USER}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/
COPY plugin.jupyterlab-settings /home/${NB_USER}/.jupyter/lab/user-settings/@jupyterlab/terminal-extension/

WORKDIR "${HOME}"
