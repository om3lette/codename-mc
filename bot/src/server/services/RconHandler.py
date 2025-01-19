import logging

import aiomcrcon
from src.constants import SERVER_ADDRESS, RCON_PORT
from unidecode import unidecode


class RconHandler:
    def __init__(self, rcon_password: str):
        self.__password: str = rcon_password
        self.__address: str = SERVER_ADDRESS.split(':')[0]

    @property
    def is_configured(self):
        return self.__password is not None and self.__password != ""

    async def execute(self, command: str) -> str | None:
        # Remove "/" from command if present, convert all Unicode characters to ascii (it is required)
        command: str = unidecode(command.replace('/', '', 1))
        try:
            async with aiomcrcon.Client(self.__address, self.__password, RCON_PORT) as client:
                return await client.command(command)
        except (OSError, TimeoutError, UnicodeEncodeError) as e:
            if e == OSError:
                logging.critical("Unable to connect to rcon. Check firewall settings and port availability")
            elif e == UnicodeEncodeError:
                logging.critical("Failed to convert string to ascii characters")
            else:
                logging.critical("Unable to connect to rcon. Connection timed out. Check the provided SERVER_ADDRESS for errors")
            return None