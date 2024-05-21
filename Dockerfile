FROM jenkins/ssh-agent:alpine-jdk17

## Install docker

RUN apk update && \
    apk add --no-cache docker
