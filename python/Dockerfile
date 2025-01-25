FROM python:3.12-alpine

ARG BOT_FOLDER_NAME

WORKDIR /app/python

COPY gen gen
COPY bots/common bots/common
COPY bots/$BOT_FOLDER_NAME bots/$BOT_FOLDER_NAME

RUN pip install --no-cache-dir --upgrade --no-cache-dir -r ./bots/$BOT_FOLDER_NAME/requirements.txt && \
    python3 -m pip uninstall pip -y

WORKDIR /app

ENTRYPOINT ["python3", "-m", "python.bots.telegram.src.main"]
