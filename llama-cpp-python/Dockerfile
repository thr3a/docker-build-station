# 参考 https://github.com/abetlen/llama-cpp-python/blob/main/docker/cuda_simple/Dockerfile
FROM --platform=linux/x86_64 thr3a/cuda12.1-torch

ENV HOST 0.0.0.0

RUN python3 -m pip install --upgrade pip fastapi uvicorn sse-starlette pydantic-settings starlette-context transformers sentencepiece

# RUN CMAKE_ARGS="-DGGML_CUDA=on -DLLAVA_BUILD=off" pip install llama-cpp-python
RUN pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

CMD python3 -m llama_cpp.server
