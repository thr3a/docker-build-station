FROM nginx:stable-alpine-slim

ENV FORWARD_HOST=host.docker.internal
ENV FORWARD_PORT=3000
ENV BASIC_USERNAME=user
ENV BASIC_PASSWORD=password

WORKDIR /app

RUN apk add --no-cache apache2-utils

COPY default.conf.template /etc/nginx/templates/
COPY generate-htpasswd.sh /docker-entrypoint.d
