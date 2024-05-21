#!/bin/bash

PUB_KEY=$(cat $PUB_KEY_PATH) # Define PUB_KEY_PATH as an environment variable
AGENT_NAME="perf"

echo $PUB_KEY

docker run -d --rm --name=$AGENT_NAME -p 4022:22 \
-e "JENKINS_AGENT_SSH_PUBKEY=$PUB_KEY" \
-v "/var/run/docker.sock:/var/run/docker.sock:rw" \
--privileged \
jenkins-agent:1.0 