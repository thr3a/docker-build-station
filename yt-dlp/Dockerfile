FROM denoland/deno:bin AS deno-bin
FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on
ENV PYTHONDONTWRITEBYTECODE=1

# No supported JavaScript runtime could be found. YouTube extraction without a JS runtime has been deprecated対策
# ref: https://github.com/yt-dlp/yt-dlp/wiki/EJS
COPY --from=deno-bin /deno /usr/local/bin/deno

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg ca-certificates && \
    rm -rf /var/lib/apt/lists/*
RUN pip install "yt-dlp[default,curl-cffi] @ https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz"
RUN pip install https://github.com/ytdl-org/youtube-dl/archive/master.tar.gz
RUN pip install https://github.com/soimort/you-get/archive/master.tar.gz

ADD yt-dlp.conf /etc/yt-dlp.conf
ADD yt-dlp.conf /etc/youtube-dl.conf

ADD https://raw.githubusercontent.com/smalltownjj/yt-dlp-plugin-missav/refs/heads/main/yt_dlp_plugins/extractor/missav.py /etc/yt-dlp-plugins/yt-dlp-plugin-missav/yt_dlp_plugins/extractor/missav.py
ADD ./dianalive.py /etc/yt-dlp-plugins/yt-dlp-plugin-dianalive/yt_dlp_plugins/extractor/dianalive.py
ADD ./doodstream.py /etc/yt-dlp-plugins/yt-dlp-plugin-doodstream/yt_dlp_plugins/extractor/doodstream.py
RUN sed -i 's/ws/ai/g' /etc/yt-dlp-plugins/yt-dlp-plugin-missav/yt_dlp_plugins/extractor/missav.py

WORKDIR /app

ENTRYPOINT ["yt-dlp"]
