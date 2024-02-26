FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz && \
    curl -LsS https://github.com/ytdl-patched/youtube-dl/releases/latest/download/youtube-dl > /usr/local/bin/youtube-dl && \
    curl -LsS https://github.com/ytdl-patched/ytdl-patched/releases/latest/download/ytdl-patched > /usr/local/bin/ytdl-patched

ADD yt-dlp.conf /etc/yt-dlp.conf
ADD yt-dlp.conf /etc/youtube-dl.conf

# https://github.com/smalltownjj/yt-dlp-plugin-missav
ADD missav.py /etc/yt-dlp-plugins/yt-dlp-plugin-missav/yt_dlp_plugins/extractor/missav.py
WORKDIR /app

ENTRYPOINT ["yt-dlp"]
