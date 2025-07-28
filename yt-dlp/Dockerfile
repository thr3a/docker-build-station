FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=on
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg ca-certificates && \
    rm -rf /var/lib/apt/lists/*
RUN pip install "yt-dlp[default,curl-cffi] @ https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz"
RUN pip install https://github.com/ytdl-org/youtube-dl/archive/master.tar.gz
RUN pip install https://github.com/soimort/you-get/archive/master.tar.gz

ADD yt-dlp.conf /etc/yt-dlp.conf
ADD yt-dlp.conf /etc/youtube-dl.conf

ADD https://raw.githubusercontent.com/smalltownjj/yt-dlp-plugin-missav/refs/heads/main/yt_dlp_plugins/extractor/missav.py /etc/yt-dlp-plugins/yt-dlp-plugin-missav/yt_dlp_plugins/extractor/missav.py
RUN sed -i 's/ws/ai/g' /etc/yt-dlp-plugins/yt-dlp-plugin-missav/yt_dlp_plugins/extractor/missav.py
WORKDIR /app

ENTRYPOINT ["yt-dlp"]
