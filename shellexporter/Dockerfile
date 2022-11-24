FROM alpine:3.14
RUN apk add --no-cache go git jq bash make
RUN mkdir /usr/local/shellexporter

workdir /usr/local/shellexporter

RUN git clone https://github.com/dodopizza/prometheus-shell-exporter.git  ./
RUN sleep 60

#RUN go get zerolog client_golang errors 


EXPOSE 9360
#CMD sleep 120
#ENTRYPOINT ["/usr/bin/go run cmd/shell-exporter/exporter.go --f metrics"]
CMD make -f makefile run
