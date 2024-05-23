FROM jenkins/inbound-agent:alpine as jnlp

FROM alpine/helm

USER root

RUN apk -U add openjdk11-jre

RUN adduser -h /home/jenkins -S jenkins 

USER jenkins

COPY --from=jnlp /usr/local/bin/jenkins-agent /usr/local/bin/jenkins-agent
COPY --from=jnlp /usr/share/jenkins/agent.jar /usr/share/jenkins/agent.jar

ENTRYPOINT ["/usr/local/bin/jenkins-agent"]
