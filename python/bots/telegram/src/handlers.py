from python.bots.telegram.src.buttons.services import PaginatorFactory
from python.bots.telegram.src.server.services import ConnectionHandler
from python.bots.telegram.src.server.services import RconHandler
from python.bots.telegram.src.constants import config

connection_handler: ConnectionHandler = ConnectionHandler(str(config.server.address))
rcon_handler: RconHandler = RconHandler(str(config.server.address), config.rcon)
paginator_factory: PaginatorFactory = PaginatorFactory()
