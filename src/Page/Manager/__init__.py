from src.Manager import Manager
from src.Page import Page
from src.Page.Manager.save_page import *

class PageManager(Manager):
    def __init__(self, lst: list[str]) -> None:
        super().__init__()
        self.current_page = Page()
        self.page_type = lst

    def set_current_page(self,page) -> None:
        self.current_page.on_exit()
        self.current_page = page

    def switch_page(self, types) -> None:
        self.current_page.on_exit()
        for i in self.page_type:
            if i == types:
                self.current_page = get_page(i)
        self.current_page.on_enter()

    def on_enter(self) -> None:
        self.current_page.on_enter()

    def on_update(self) -> None:
        self.current_page.on_update()

    def on_draw(self) -> None:
        self.current_page.on_draw()

    def on_input(self, event) -> None:
        self.current_page.on_input(event)

    def on_exit(self) -> None:
        self.current_page.on_exit()