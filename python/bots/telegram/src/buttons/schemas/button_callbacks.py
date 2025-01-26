from aiogram.filters.callback_data import CallbackData


class PaginationNav(CallbackData, prefix="pag_nav"):
	action: str = "page_change"
	page: int
