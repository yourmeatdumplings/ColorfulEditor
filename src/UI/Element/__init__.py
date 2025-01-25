import pygame.event


class Element:
    def __init__(self, state: bool = True):
        self.state = state

        self.parent = None

        self.elements = {}

        self.x = 0
        self.y = 0
        self.out_x = 0
        self.out_y = 0
        self.world_x = 0
        self.world_y = 0

    def add(self, __id, element):
        try:
            temp = self.elements[__id]
            print(f'{__id} in!')
        except KeyError:
            try:
                element.parent = self
                self.elements[__id] = element
            except KeyError:
                print(666)
    def on_update(self):
        if self.elements:
            for elem in self.elements.values():
                elem.on_update()
    def on_input(self, event: pygame.event.Event):
        if self.elements:
            for elem in self.elements.values():
                elem.on_input(event)
    def draw_son(self, ui):
        if self.elements:
            for elem in self.elements.values():
                if elem.state:
                    elem.on_draw(ui)
                    elem.draw_son(ui)
    def on_draw(self, ui):
        if self.parent:
            self.world_x, self.world_y = (self.x + self.out_x + self.parent.world_x, self.y + self.out_y + self.parent.world_y)
        else:
            self.world_x, self.world_y = self.x, self.y

