# docker-build-station

### Dockerhub

https://hub.docker.com/u/thr3a

### Github Container Registry

https://github.com/thr3a?tab=packages&repo_name=docker-build-station

# 追加方法

- ディレクトリを新規作成してDockerfileを作る
- jobs.build-and-push-image.strategy.matrix.targetにディレクトリ名を追記

# GPU系テンプレ

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
FROM thr3a/cuda12.8-torch:latest

WORKDIR /app
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  apt update && apt-get --no-install-recommends install -y ffmpeg

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv,sharing=locked \
    uv sync --locked --no-dev --no-install-project

COPY README.md LICENSE ./
COPY src ./src

RUN --mount=type=cache,target=/root/.cache/uv,sharing=locked \
    uv sync --locked --no-dev --no-editable --no-cache

# COPY ./requirements.txt ./
# RUN pip install -r requirements.txt
```


# 参考リンク

- [HTTP/3が喋れるcurlを定期的にbuildする | うなすけとあれこれ](https://blog.unasuke.com/2021/curl-http3-daily-build/)
- [GitHub Actionsで複数のDockerfileをまとめてビルド - Qiita](https://qiita.com/tomoyk/items/ab4d55cd1735bb2b579a)

- [Dockerイメージの公開 - GitHub Docs](https://docs.github.com/ja/actions/publishing-packages/publishing-docker-images)

2026/08/01
