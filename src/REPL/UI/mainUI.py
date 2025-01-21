from src.UI import UI
from src.UI.Element.input import Input

class MainUI(UI):
    def __init__(self, state: bool = True):
        super().__init__(state)

    def init(self):
        self.add('input', Input(size=60, cursor_color='green', cursor_flicker=False))