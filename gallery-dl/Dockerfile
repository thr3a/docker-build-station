FROM thr3a/yt-dlp:latest

# https://github.com/mikf/gallery-dl/issues/5665
RUN pip install https://github.com/mikf/gallery-dl/archive/refs/heads/master.tar.gz 'requests<2.32'


ENTRYPOINT ["gallery-dl"]
