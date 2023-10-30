#!/bin/bash/

CONTAINER_NAME="density_analysis"
IMAGE_NAME="density_analysis"
TAG="0.1"


docker run \
    --runtime nvidia \
    --gpus all \
    -it \
    -p 10000:8000 \
    -p 10001:8080 \
    -p 10002:8888 \
    --name ${CONTAINER_NAME} \
    -v your volume\
    ${IMAGE_NAME}:${TAG}

