FROM jenkins/inbound-agent:alpine as jnlp

FROM python:3.10-alpine3.19

RUN apk -U add openjdk11-jre git gcc musl-dev linux-headers

RUN adduser -h /home/jenkins -S jenkins

RUN pip3 install locust==2.28.0

USER jenkins

COPY --from=jnlp /usr/local/bin/jenkins-agent /usr/local/bin/jenkins-agent
COPY --from=jnlp /usr/share/jenkins/agent.jar /usr/share/jenkins/agent.jar

ENTRYPOINT ["/usr/local/bin/jenkins-agent"]
