PING_SUCCESS: str = "Статус сервера: ✅\nЗадержка: {latency}мс ⌛"
PING_ERROR: str = (
	"Попытка №{attempt_number} ❌\nПовтор через {time_before_retry} секунд ⌛"
)
PING_HANGUP: str = "Статус сервера: 😵\nВызываю админов:\n{admins}"
PING_HANGUP_ADMIN: str = (
	"Статус сервера: 😵 ️\nТребуется ручная проверка 🔧\nСервер: {server_name} 🖥️"
)

PLAYERS_NUMBER: str = "Игроков на сервере: {current_number}/{capacity}📶"
PLAYERS_ONLINE: str = "Игроки на сервере 🎮"

QUERY_NOT_ENABLED_ERROR_MESSAGE: str = (
	"Не удалось выполнить запрос 😞\n"
	"В `server\.properties` необходимо задать следующие параметры:"
	"```config\nenable_query=true\nserver_ip=<ip_сервера>```"
	"*Для этого шага требуется перезагрузка сервера\!*"
)
NO_PLAYERS_ONLINE: str = "Тут никого нет 😭"
NO_ADMINS_FOUND: str = "Админы для сервера не указаны 😢"

PERMISSION_LEVEL_TOO_LOW: str = "Недостаточно прав для совершения действия"
INCORRECT_RCON_COMMAND_FORMAT: str = (
	"Некорректный формат ввода```\n/execute <команда>```"
)
GENERAL_FAILURE: str = "Произошла ошибка 🫣"
FEATURE_WAS_NOT_SETUP: str = "Данная функция выключена или настроена некорректно😞\nПопросите администраторов выполнить условия для её работы"

COMMAND_EXECUTED_SUCCESSFULLY: str = "Команда успешно выполнена!"
