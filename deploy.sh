#!/bin/bash
cd bitbotpy && \
git pull && \
cd ../ && \
# docker image rm bitbotpy:latest && \
docker build -t bitbotpy:latest . && \
docker run --rm  -p 80:80 --name bitbotpy bitbotpy:latest