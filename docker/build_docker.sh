#!/bin/bash/

IMAGE_NAME="density_analysis"
TAG="0.1"

docker build -t ${IMAGE_NAME}:${TAG} .

