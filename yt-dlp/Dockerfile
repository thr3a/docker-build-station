FROM python:3

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz && \
    curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
    chmod +x /usr/local/bin/youtube-dl

ADD yt-dlp.conf /etc/yt-dlp.conf
ADD yt-dlp.conf /etc/youtube-dl.conf

WORKDIR /app

ENTRYPOINT ["yt-dlp"]
