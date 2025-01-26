from pydantic import BaseModel, Field, IPvAnyAddress
from pathlib import Path
import yaml
from typing import Self

try:
	from yaml import CLoader as Loader
except ImportError:
	from yaml import Loader


class ServerConfigSchema(BaseModel):
	name: str = Field(default="Minecraft server")
	address: IPvAnyAddress = Field(default="127.0.0.1")
	port: int = Field(default=25565)


class ConnectionConfigSchema(BaseModel):
	max_retries_before_hangup: int = Field(default=3)
	seconds_between_retries: int = Field(default=20)


class AdminsConfigSchema(BaseModel):
	usernames: list[str] = []
	ids: list[int] = []


class RconConfigSchema(BaseModel):
	password: str | None = Field(default=None)
	port: int = Field(default=25575)


class ConfigSchema(BaseModel):
	bot_token: str
	server: ServerConfigSchema = Field(default_factory=ServerConfigSchema)
	admins: AdminsConfigSchema = Field(default_factory=AdminsConfigSchema)
	connection: ConnectionConfigSchema = Field(default_factory=ConnectionConfigSchema)
	rcon: RconConfigSchema = Field(default_factory=RconConfigSchema)
	dev_mode: bool = Field(default=False)

	def model_save_yaml(self, save_path: Path) -> None:
		with open(save_path, "w") as f:
			f.write(yaml.dump(self.model_dump()))

	@classmethod
	def from_yaml(cls, config_path: Path) -> Self:
		if config_path.is_file() and config_path.suffix != ".yaml":
			raise FileNotFoundError
		if not config_path.is_file():
			ConfigSchema(bot_token="<YOUR_BOT_TOKEN>").model_save_yaml(config_path)
			raise FileNotFoundError
		with open(config_path, "r") as config_file:
			data = yaml.load(config_file, Loader)
		return cls.model_validate(data)
