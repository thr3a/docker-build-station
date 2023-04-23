# https://github.com/weseek/growi-docker-compose/blob/master/elasticsearch/Dockerfile
ARG version=7.17.1
FROM docker.elastic.co/elasticsearch/elasticsearch:${version}

RUN bin/elasticsearch-plugin install analysis-kuromoji
RUN bin/elasticsearch-plugin install analysis-icu

ADD ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml
