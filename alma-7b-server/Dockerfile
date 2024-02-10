FROM ghcr.io/ggerganov/llama.cpp:server

RUN apt-get update \
  && apt-get install -y --no-install-recommends curl ca-certificates \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -sL https://huggingface.co/mmnga/webbigdata-ALMA-7B-Ja-V2-gguf/resolve/main/webbigdata-ALMA-7B-Ja-V2-q4_K_M.gguf > model.gguf

ENTRYPOINT ["/server", "-m", "model.gguf", "--host", "0.0.0.0", "--port", "30000"]
