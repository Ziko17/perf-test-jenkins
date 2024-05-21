FROM jenkins/ssh-agent:alpine-jdk17

## Install docker

RUN apk add --update docker openrc