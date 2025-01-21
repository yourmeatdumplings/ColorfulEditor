from src.Page import Page
from src.Page.Manager.save_page import *
from src.REPL.UI.mainUI import MainUI
from src.UI.manger import UIManger

class REPLPage(Page):
    def __init__(self):
        super().__init__()
        self.page_manager = get_page('manager')

        self.ui_manger = UIManger()
        self.ui_manger.add('main', MainUI(True))

    def on_enter(self):
        ...

    def on_update(self):
        self.ui_manger.on_update()

    def on_input(self, event):
        self.ui_manger.on_input(event)

    def on_draw(self):
        self.ui_manger.on_draw()

    def on_exit(self): ...