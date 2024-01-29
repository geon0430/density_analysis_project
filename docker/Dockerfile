FROM ubuntu:latest

ENV TZ=Asia/Seoul

RUN mkdir -p /workspace
WORKDIR /workspace

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    ln -s $(which python3) /usr/bin/python && \
    apt-get install -y libglib2.0-0 && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get install -y vim && \
    apt-get install -y tmux && \
    apt-get install -y git && \
    pip install jupyter 

CMD ["bash"]

