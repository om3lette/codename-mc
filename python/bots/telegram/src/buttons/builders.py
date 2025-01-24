import python.bots.telegram.src.buttons.schemas.paginator_configs as configs
from python.bots.telegram.src.buttons.services.PaginatorFactory import PaginatorBuilder
from python.bots.telegram.src.handlers import paginator_factory

players_markup_builder: PaginatorBuilder = paginator_factory.create_builder(configs.player_pag_config)
