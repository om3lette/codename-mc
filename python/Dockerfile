FROM ubuntu:22.04 AS builder

ARG BOT_FOLDER_NAME
WORKDIR /app/python

COPY gen gen
COPY bots/common bots/common
COPY bots/$BOT_FOLDER_NAME bots/$BOT_FOLDER_NAME

RUN rm -f gen/generate_grpc.sh

WORKDIR /app
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

FROM python:3.12-alpine

WORKDIR /app
ARG BOT_FOLDER_NAME
ENV BOT_FOLDER_NAME=${BOT_FOLDER_NAME}
COPY --from=builder /app /app
RUN pip install --no-cache-dir --upgrade --no-cache-dir -r python/bots/$BOT_FOLDER_NAME/requirements.txt \
    && python3 -m pip uninstall pip -y

ENTRYPOINT ["./entrypoint.sh"]
