class Page:
    def __init__(self):
        self.state = False
    def on_enter(self): ...
    def on_exit(self): ...
    def on_update(self): ...
    def on_input(self, event): ...
    def on_draw(self): ...