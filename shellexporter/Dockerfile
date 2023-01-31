FROM alpine:3.14
RUN apk add --no-cache go git jq bash make
RUN mkdir /usr/local/shellexporter

workdir /usr/local/shellexporter

RUN git clone https://github.com/dodopizza/prometheus-shell-exporter.git  ./

EXPOSE 9360

CMD make -f makefile run
