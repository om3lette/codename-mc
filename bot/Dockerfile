FROM python:3.12-alpine

COPY . /bot

WORKDIR /bot
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["python3", "-m", "src.main"]