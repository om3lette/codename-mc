## Использование линтера / форматтера

### Установка зависимостей
```bash
pip install --upgrade -r python/devb-requirements
```
```bash
ruff format python/ --config python/ruff.toml && ruff check python/ --config python/ruff.toml
```

## Сборка Docker образа

Все команды, указанные далее, предполагают исполнение из корня проекта

### gRPC
До начала сборки необходимо сгенерировать код gRPC для Python
```bash
pip install --upgrade -r python/gen/grpc-requirements.txt \
&& bash python/gen/generate_grpc.sh
```

### ARGS

1. `BOT_FOLDER_NAME` - название папки в `/python/bots/`, которую необходимо скопировать в контейнер. Возможные варианты: `telegram`

```bash
docker build -t server-guard-tg --build-arg "BOT_FOLDER_NAME=telegram" ./python/
```