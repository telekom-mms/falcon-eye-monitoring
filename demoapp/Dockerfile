FROM maven:3.8.6

MAINTAINER T-Systems MMS

ENV OTEL_VERSION=1.19.2

WORKDIR /usr/local/opentelemetry

RUN wget https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v${OTEL_VERSION}/opentelemetry-javaagent.jar

WORKDIR /usr/local/spring-petclinic

RUN git clone https://github.com/spring-projects/spring-petclinic.git .
RUN MAVEN_CONFIG= ./mvnw package

EXPOSE 8080

CMD java \
-javaagent:/usr/local/opentelemetry/opentelemetry-javaagent.jar \
-Dotel.exporter.otlp.endpoint=https://fem_otel-collector:4318 \
-Dotel.exporter.otlp.certificate=/tmp/certs/server.crt \
-Dotel.resource.attributes=service.name=demoapp \
-Dotel.metrics.exporter=otlp \
-Dotel.logs.exporter=otlp \
-jar target/*.jar