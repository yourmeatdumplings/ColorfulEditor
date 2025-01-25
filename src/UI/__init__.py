import pygame

from src.UI.Element import Element


class UI:
    def __init__(self, state: bool = False):
        self.state = state

        self.surface_display = pygame.display.get_surface()

        self.elements: dict[str, Element] = {}

        self.init()
    def init(self): ...
    def add(self, __id, element):
        try:
            temp = self.elements[__id]
            print(f'{__id} in!')
        except KeyError:
            try:
                self.elements[__id] = element
            except KeyError:
                print(666)
    def open(self):
        self.state = True
    def close(self):
        self.state = False
    def get(self, __id) -> Element | None:
        try:
            return self.elements[__id]
        except KeyError:
            return None
    def on_update(self):
        for elem in self.elements.values():
            elem.on_update()
    def on_input(self, event):
        for elem in self.elements.values():
            elem.on_input(event)
    def on_draw(self):
        for elem in self.elements.values():
            if elem.state:
                elem.on_draw(self)
                elem.draw_son(self)