docker-compose.yml

```yml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: peft-workspace:latest
    stop_grace_period: 0s
    ipc: host
    tty: true
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              device_ids: ['1']
              capabilities: [gpu]
    volumes:
      - "./:/app"
      - "./cache:/root/.cache"
    # command: sleep infinity
    command: python train_rinna.py
```

Dockerfile

```dockerfile
FROM thr3a/cuda12.6-torch:latest

WORKDIR /app
# COPY ./requirements.txt ./
# RUN pip install -r requirements.txt

COPY pyproject.toml ./
COPY uv.lock ./
RUN uv sync --frozen --no-cache
```
