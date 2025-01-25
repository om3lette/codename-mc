# ServerGuard

## Настройка сервера

Работоспособность некоторых команд зависит от настройки сервера (`server.properties`)

### Для использования команд: `В разработке`

Включить query `enable_query=true`, по необходимости указать ip сервера `server_ip=<ip_сервера>`

### Для использования команд: `execute`

Включить rcon: `enable_rcon=true`\
Задать пароль: `rcon_password=<YOUR_PASSWORD>`

## Функционал

- [x] Просмотр статуса сервера (офлайн/онлайн)
- [x] Просмотр количества игроков на сервере
- [x] Просмотр имен игроков на сервере
- [x] Оповещение админов о падении сервера в случае офлайн статуса
- [x] Удаленное исполнение команд администраторами

## Как запустить

1. Установите зависимости 
```commandline
pip install -r requirements.txt
```
2. Запустите локально

### Python
Создайте конфигурационный файл вручную или запустите бота, в этом случае шаблонный конфигурационный файл сгенерируется самостоятельно\
Следующие команды необходимо выполнять их корня проекта `/`

#### Windows
```commandline
python -m python.bots.telegram.src.main
```

#### Linux
```commandline
python3 -m python.bots.telegram.src.main
```

### Docker
Сборку образа можно осуществить с помощью `/python/Dockerfile`\
Запуск контейнера
```commandline
sudo docker run -d --rm --name server-guard -v <YOUR_PATH_TO_CONFIG>/config.yaml:/app/config.yaml server-guard
```
При использовании `compose` рекомендуется объединить сервер и `ServerGuard` в одном `compose` файле при условии, что сервер также запущен с использованием `Docker`
