FROM php:7.4-fpm

ENV IPE_GD_WITHOUTAVIF=1
ENV TZ=Asia/Tokyo
ENV COMPOSER_ALLOW_SUPERUSER=1

ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions \
    gd-stable \
    xdebug-stable \
    intl-stable \
    mysqli-stable \
    pdo_mysql-stable \
    redis-stable \
    @composer

WORKDIR /app
COPY ./myphp.ini /usr/local/etc/php/conf.d/myphp.ini
