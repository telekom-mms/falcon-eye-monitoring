FROM alpine:3.17.2

ENV SHELLEXPORTER_VERSION=0.1.15

RUN apk add --no-cache go git jq bash make
RUN mkdir /usr/local/shellexporter

WORKDIR /usr/local/shellexporter

RUN git clone --branch ${SHELLEXPORTER_VERSION} https://github.com/dodopizza/prometheus-shell-exporter.git ./

EXPOSE 9360

CMD make -f makefile run
