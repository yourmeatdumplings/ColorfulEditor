from src.UI import UI
from src.UI.Element.base import Base
from src.UI.Element.input import Input
from src.UI.Element.text_base import TextBase

class MainUI(UI):
    def __init__(self, state: bool = True):
        super().__init__(state)

    def init(self):
        input_elem = Input(size=60)
        self.add('input', input_elem)