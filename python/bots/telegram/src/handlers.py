from python.bots.telegram.src.buttons.services.PaginatorFactory import PaginatorFactory
from python.bots.telegram.src.server.services.ConnectionHandler import ConnectionHandler
from python.bots.telegram.src.server.services.RconHandler import RconHandler
from python.bots.telegram.src.constants import config

connection_handler: ConnectionHandler = ConnectionHandler(str(config.server.address))
rcon_handler: RconHandler = RconHandler(str(config.server.address), config.rcon)
paginator_factory: PaginatorFactory = PaginatorFactory()
