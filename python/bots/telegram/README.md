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
1. Склонировать репозиторий
```bash
git clone https://github.com/om3lette/ServerGuard.git
```
2. Установите зависимости 
```commandline
pip install -r requirements.txt
```
3. Запустите локально
### Python
Укажите переменные окружения в команде для в `.env`
#### Windows
```
python -m src.main
```
#### Linux
```commandline
python3 -m src.main
```
### Docker
```commandline
sudo docker build -t server-guard .
```
Или из репозитория
```commandline
sudo docker build -t server-guard https://github.com/om3lette/ServerGuard.git
```
Укажите переменные окружения в команде для `Docker` и запустите
```commandline
sudo docker run -d --rm --name server-guard \
-e SERVER_ADDRESS "<YOUR_VALUE>" \
-e BOT_TOKEN "<YOUR_TOKEN>" \
-e ADMINS "<OPTIONAL>" \
-e ADMIN_IDS "<OPTIONAL>" \
-e RCON_PASSWORD "<OPTIONAL>" \
-e RCON_PORT <OPTIONAL> \
-e SERVER_NAME "<OPTIONAL>"
server-guard
```
Также доступен `compose.yaml` файл для запуска образа.\
При использовании `compose` рекомендуется объединить сервер и `ServerGuard` в одном `compose` файле при условии, что сервер также запущен с использованием `Docker`