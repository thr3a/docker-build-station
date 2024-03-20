docker-compose.yml

```yml
version: "3"

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
