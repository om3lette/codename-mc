from collections.abc import Callable

from pydantic import BaseModel, Field

class PaginatorConfig(BaseModel):
    item_to_text: Callable[[any, int], str]
    items_per_row: int = Field(default=3)
    number_of_rows: int = Field(default=2)
    click_callback: Callable | None = Field(default=None)
