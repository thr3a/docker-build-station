FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg && \
    rm -rf /var/lib/apt/lists/*
RUN pip install https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
RUN pip install https://github.com/ytdl-org/youtube-dl/archive/master.tar.gz
RUN pip install https://github.com/soimort/you-get/archive/master.tar.gz

ADD yt-dlp.conf /etc/yt-dlp.conf
# ADD yt-dlp.conf /etc/youtube-dl.conf

# https://github.com/smalltownjj/yt-dlp-plugin-missav
ADD missav.py /etc/yt-dlp-plugins/yt-dlp-plugin-missav/yt_dlp_plugins/extractor/missav.py
WORKDIR /app

ENTRYPOINT ["yt-dlp"]
