FROM openjdk:8

RUN apt-get update \
  && apt-get install -y --no-install-recommends wget unzip p7zip-full \
  && rm -rf /var/lib/apt/lists/*

ENV JD_VERSION="1.4.0"
#ENV JD_VERSION="1.6.6"
# ENV JD_CLI_VERSION="1.2.0"
ENV JD_CLI_VERSION="0.9.1.Final"

WORKDIR /opt

# Dex2Jar
RUN wget -q -O dex2jar.zip https://github.com/pxb1988/dex2jar/releases/download/v2.4/dex-tools-v2.4.zip \
    && unzip dex2jar.zip \
    && chmod u+x dex-tools-v2.4/*.sh \
    && rm -f dex2jar.zip
ENV PATH=$PATH:/opt/dex-tools-v2.4

# JD-GUI
RUN wget -q -O jd-gui.jar "https://github.com/java-decompiler/jd-gui/releases/download/v$JD_VERSION/jd-gui-$JD_VERSION.jar"

# JD-CLI
RUN wget -q -O jd-cli.zip "https://github.com/intoolswetrust/jd-cli/releases/download/jd-cmd-$JD_CLI_VERSION/jd-cli-$JD_CLI_VERSION-dist.zip" \
  && unzip jd-cli.zip \
  && rm -f jd-cli.zip

COPY extract.sh .
RUN chmod +x extract.sh

WORKDIR /app

ENTRYPOINT ["bash", "/opt/extract.sh"]
