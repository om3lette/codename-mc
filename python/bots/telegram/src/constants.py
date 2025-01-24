from python.bots.common import ConfigSchema
from pathlib import Path

CONFIG_PATH: Path = Path(__file__).parents[1].joinpath("config.yaml")
config: ConfigSchema = ConfigSchema.from_yaml(CONFIG_PATH)
