FROM ghcr.io/thr3a/cuda12.1-torch:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
  libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx \
  && rm -rf /var/lib/apt/lists/*

RUN pip install iopaint rembg
RUN iopaint download --model=lama
ENTRYPOINT ["iopaint", "start", "--model=lama", "--device=cuda", "--host=0.0.0.0", "--port=8080", "--enable-remove-bg"]

