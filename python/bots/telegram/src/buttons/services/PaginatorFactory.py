import math
import logging
from logging import Logger
from enum import IntEnum

import python.bots.telegram.src.buttons.schemas.button_callbacks as callbacks

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from python.bots.telegram.src.buttons.schemas.PaginatorConfig import PaginatorConfig

logger: Logger = logging.getLogger()

class PaginatorExitStatus(IntEnum):
    OK = 0
    ALREADY_UP_TO_DATE = 1

class PaginatorBuilder:
    prev_page_index: int = -1

    def __init__(self, config: PaginatorConfig):
        self.config: PaginatorConfig = config

    def build(self, data: list[any], page_index: int, force_render: bool = False) -> [InlineKeyboardMarkup, PaginatorExitStatus]:
        if self.prev_page_index == page_index and not force_render:
            return None, PaginatorExitStatus.ALREADY_UP_TO_DATE
        keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        items_per_page: int = self.config.items_per_row * self.config.number_of_rows

        page_start_index: int = page_index * items_per_page
        page_end_index: int = min(page_start_index + items_per_page, len(data))
        total_pages: int = math.ceil(len(data) / items_per_page)

        current_page_items: list[any] = data[page_start_index:page_end_index]
        rows_to_add: int = math.ceil(len(current_page_items) / self.config.items_per_row)

        page_index_human: int = min(page_index + 1, total_pages)
        logging.debug(f"Markup update. Current page: {page_index_human}/{total_pages}. Elements to display: {len(current_page_items)}. Added rows: {rows_to_add}")
        for i in range(rows_to_add):
            start_index: int = self.config.items_per_row * i
            buttons: list[InlineKeyboardButton] = [
                InlineKeyboardButton(text=self.config.item_to_text(current_page_items[j], j), callback_data="skip")
                for j in range(start_index, min(start_index + self.config.items_per_row, len(current_page_items)))
            ]
            keyboard_builder.row(*buttons)

        nav_buttons_row: list[InlineKeyboardButton] = []

        # Go to the previous page
        prev_page_index: int = page_index - 1 if page_index != 0 else total_pages - 1
        nav_buttons_row.append(InlineKeyboardButton(
            text="⬅️",
            callback_data=callbacks.PaginationNav(action="prev", page=prev_page_index).pack())
        )
        nav_buttons_row.append(InlineKeyboardButton(text=f"{page_index_human}/{total_pages}", callback_data="skip"))
        # Go to the next page
        next_page_index: int = page_index + 1 if page_index != total_pages - 1 else 0
        nav_buttons_row.append(InlineKeyboardButton(
            text="➡️",
            callback_data=callbacks.PaginationNav(action="next", page=next_page_index).pack())
        )
        keyboard_builder.row(*nav_buttons_row)
        # Todo: Close / go back
        # keyboard_builder.row(InlineKeyboardButton())

        self.prev_page_index = page_index
        return keyboard_builder.as_markup(), PaginatorExitStatus.OK

# TODO: Singleton
class PaginatorFactory:
    @staticmethod
    def create_builder(config: PaginatorConfig) -> PaginatorBuilder:
        return PaginatorBuilder(config)
