FROM ghcr.io/thr3a/cuda12.1-torch:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
  libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U iopaint rembg[gpu]
RUN iopaint download --model=lama
RUN python -c "from iopaint.plugins.anime_seg import AnimeSeg; AnimeSeg()"
RUN python -c "from iopaint.plugins.briarmbg2 import create_briarmbg2_session;create_briarmbg2_session()"
ENTRYPOINT ["iopaint"]
CMD ["start", "--device=cuda", "--host=0.0.0.0", "--port=8080", "--enable-remove-bg", "--remove-bg-model", "briaai/RMBG-2.0"]
