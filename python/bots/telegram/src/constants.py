from python.bots.common import ConfigSchema
from pathlib import Path

# If root dir is named app than bot is running in docker container.
# Fetch config from the root folder
CONFIG_PARENT_INDEX: int = 3 if Path(__file__).parents[4].name != "app" else 4
CONFIG_PARENT_DIR: Path = Path(__file__).parents[CONFIG_PARENT_INDEX]

# /python/config.yaml in dev
# /app/config.yaml in prod
CONFIG_PATH: Path = CONFIG_PARENT_DIR.joinpath("config.yaml")

config: ConfigSchema = ConfigSchema.from_yaml(CONFIG_PATH)
