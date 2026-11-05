FROM python:3.13-slim

RUN pip install --no-cache-dir comfy-api-proxy==0.1.6

EXPOSE 8189

ENTRYPOINT ["comfy-api-proxy", "run", "--host", "0.0.0.0", "--port", "8189", "--allow-insecure-bind"]
CMD ["--comfyui", "http://192.168.16.20:8188"]
