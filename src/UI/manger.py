from src.Manager import Manager
from src.UI import UI

class UIManger(Manager):
    def __init__(self):
        super().__init__()

        self.uis: dict[str, UI] = {}
    def add(self, __id, ui):
        try:
            temp = self.uis[__id]
            print(f'{__id} in!')
        except KeyError:
            try:
                self.uis[__id] = ui
            except KeyError:
                print(666)
    def open(self, __id):
        try:
            self.uis[__id].open()
        except KeyError:
            print(f'{__id} open err!')
    def close(self, __id):
        try:
            self.uis[__id].close()
        except KeyError:
            print(f'{__id} open err!')
    def get(self, __id):
        try:
            return self.uis[__id]
        except KeyError:
            return None
    def on_update(self):
        for ui in self.uis.values():
            ui.on_update()
    def on_input(self, event):
        for ui in self.uis.values():
            ui.on_input(event)
    def on_draw(self):
        if self.uis:
            for ui in self.uis.values():
                if ui.state:
                    ui.on_draw()