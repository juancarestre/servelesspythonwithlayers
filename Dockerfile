FROM python:3-alpine3.8

# docker container run --rm -it serverlessbuilder sh -c "source .venv/bin/activate && serverless invoke local --function pikachu" | jq

ENV ALPINE_MIRROR "http://dl-cdn.alpinelinux.org/alpine"

RUN echo "${ALPINE_MIRROR}/edge/main" >> /etc/apk/repositories
RUN apk add --no-cache nodejs-current  --repository="http://dl-cdn.alpinelinux.org/alpine/edge/community"
RUN node --version

RUN apk update && apk upgrade \
  && apk add bash curl make \
  && rm -rf /var/cache/apk/*

RUN apk add npm==7.13.0-r0 && \
    npm install -g serverless

RUN pip install awscli

WORKDIR /tmp

COPY ./ /tmp

RUN npm install --save

RUN python -m venv .venv
RUN source .venv/bin/activate && pip install --upgrade pip
RUN source .venv/bin/activate && pip install wheel

RUN aws configure set default.region us-east-1 && \
    aws configure set aws_access_key_id 'DUMMY_ACCESS_KEY' && \
    aws configure set aws_secret_access_key 'DUMMY_SECRET_KEY'

RUN source .venv/bin/activate && pip install -r app/shared_requeriments.txt