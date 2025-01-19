from src.buttons.services.PaginatorFactory import PaginatorFactory
from src.server.services.ConnectionHandler import ConnectionHandler
from src.server.services.RconHandler import RconHandler
from src.constants import SERVER_ADDRESS, RCON_PASSWORD

connection_handler: ConnectionHandler = ConnectionHandler(SERVER_ADDRESS)
rcon_handler: RconHandler = RconHandler(RCON_PASSWORD)
paginator_factory: PaginatorFactory = PaginatorFactory()
