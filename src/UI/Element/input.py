from typing import Any
import pygame
import string
import pyperclip
from pygame import Surface
from pygame.color import Color
from src import default_font, get_global_height
from src.Libs.display import get_global_size, get_global_width
from src.Libs.timer import CountTimer
from src.Style import InputMode, EnterMode
from src.UI.Element import Element

class Input(Element):
    def __init__(self, default_text: str = 'InputBox', mode: InputMode = InputMode.TextInputMode, enter_mode: EnterMode = EnterMode.Submit, x: int = 0, y: int = 0, width: int = 100, size: int = 20, color: str | tuple[int,int,int] | Color = 'white', is_outline: bool = True, outline_size: int = 2, outline_color: str | tuple[int,int,int] | Color= 'gray',cursor_flicker: bool = True, cursor_width: int = 2, cursor_color: str | tuple[int,int,int] | Color = 'white',cursor_flicker_interval: int = 30, start_delete: float = 0.3, delete_interval: int = 2, start_control: float = 0.3, control_interval: int = 2, choose_color: str | tuple[int,int,int] | Color = 'blue', font: str = default_font, state: bool = True):
        super().__init__(state)

        self.config: dict[str: Any] = {
            "EnableCopying": True,
            "EnablePasting": True,
            "EnableCutting": True,
            # "EnableOutline": is_outline
        }

        self.input_mode = mode
        self.enter_mode = enter_mode
        self.input_x = x
        self.input_y = y
        self.default_text = default_text
        self.text_lst: list[str] = []
        self.font = font
        self.color = color
        self.text_size = size
        self.input_width = width

        self.is_outline = is_outline
        self.input_outline_size = outline_size
        self.input_outline_color = outline_color
        self.cursor_flicker = cursor_flicker
        self.cursor_width = cursor_width
        self.cursor_flicker_interval = cursor_flicker_interval
        self.cursor_color = cursor_color
        self.start_delete = start_delete
        self.delete_interval = delete_interval
        self.start_control = start_control
        self.control_interval = control_interval
        self.choose_color = choose_color

        self.active = False
        self.cursor = True
        self.cursor_count = 0
        self.cursor_pos = 0
        self.cursor_value = []
        self.delete = False
        self.delete_count = 0
        self.start_delete_count = CountTimer(start_delete)
        self.input_event = False
        self.input_event_mode = None
        self.input_count = 0
        self.start_input_count = CountTimer(start_control)

        self.submit_func = print
        self.args = ['this submit!']
        self.kwargs = {}

        self.__mode()

    @property
    def text(self):
        return ''.join(self.text_lst)
    def set_input_x(self, __x):
        self.input_x = __x
    def set_input_y(self, __y):
        self.input_y = __y
    def add_input_x(self, __x):
        self.input_x += __x
    def add_input_y(self, __y):
        self.input_y += __y
    def get_config(self):
        for key, value in self.config.items():
            print(f'{key}: {value}')
    def set_config(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.config.keys():
                self.config[key] = value
            else:
                print(f'{key} config not!')

    def __surface(self):
        if self.text_lst:
            text = ''.join(self.text_lst)
            alpha = 255
        else:
            text = self.default_text
            alpha = 100

        font_surf = pygame.font.Font(self.font, get_global_height(self.text_size))
        self.text_surface = font_surf.render(str(text), True, self.color)
        self.text_surface.set_alpha(alpha)
        self.text_rect = self.text_surface.get_rect(topleft=get_global_size(self.input_x, self.input_y))
        if self.text_lst:
            self.box = Surface((self.text_rect.width + get_global_width(self.input_width), self.text_rect.height))
        elif self.text_rect.width > self.input_width:
            self.box = Surface((self.text_rect.width, self.text_rect.height))
        else:
            self.box = Surface((get_global_width(self.input_width), self.text_rect.height))
        self.rect = self.box.get_rect(topleft = get_global_size(self.input_x, self.input_y))

    def __mode(self):
        match self.input_mode:
            case InputMode.TextInputMode:
                self.__surface()
            case InputMode.NumberInputMode:
                self.__surface()

    def __cursor(self, ui):
        self.cursor_count += 1
        if self.cursor_count == self.cursor_flicker_interval:
            self.cursor_count = 0
            self.cursor = not self.cursor
        if self.active and (self.cursor or not self.cursor_flicker):
            width = get_global_width(self.cursor_width)
            color = self.cursor_color

            if self.text_lst:
                font = pygame.font.Font(self.font, get_global_height(self.text_size))
                i = font.size(''.join(self.text_lst[:self.cursor_pos]))[0]
                x = self.text_rect.x + i
            else:
                x = self.text_rect.x
            pygame.draw.line(ui.surface_display, color, (x, self.text_rect.y),(x, self.text_rect.y + self.text_rect.height), width)

    def __cursor_value(self, ui):
        if self.cursor_value:
            font = pygame.font.Font(self.font, get_global_height(self.text_size))
            long = self.cursor_value[0] - self.cursor_value[1]
            if long == 0:
                self.cursor_value = None
            else:
                if long > 0:
                    i = font.size(''.join(self.text_lst[:self.cursor_value[1]]))[0]

                    surf = Surface((font.size(''.join(self.text_lst[self.cursor_value[1]:self.cursor_value[0]]))[0], self.text_rect.height))

                    x, y= self.text_rect.topleft

                    rect = surf.get_rect(topleft=
                        (x + i, y)
                    )
                    pygame.draw.rect(ui.surface_display, self.choose_color, rect)
                elif long < 0:
                    i = font.size(''.join(self.text_lst[:self.cursor_value[0]]))[0]

                    surf = Surface((font.size(''.join(self.text_lst[self.cursor_value[0]:self.cursor_value[1]]))[0], self.text_rect.height))

                    x, y= self.text_rect.topleft

                    rect = surf.get_rect(topleft=
                        (x + i, y)
                    )
                    pygame.draw.rect(ui.surface_display, self.choose_color, rect)

    def __del_cursor(self):
        long = self.cursor_value[0] - self.cursor_value[1]

        if long > 0:
            for _ in range(long):
                del self.text_lst[self.cursor_value[1]]
        elif long < 0:
            for i in range(abs(long)):
                del self.text_lst[self.cursor_value[0]]
                self.cursor_pos -= 1

        self.cursor_value = None

    def __del(self):
        if self.start_delete_count.is_done():
            self.delete = True
        if self.active and self.delete:
            self.delete_count += 1
            if self.delete_count == self.delete_interval:
                self.delete_count = 0
                self.__del_text()

    def __input(self):
        if self.start_input_count.is_done():
            self.input_event = True
        if self.active and self.input_event:
            self.input_count += 1
            if self.input_count == self.control_interval:
                self.input_count = 0
                self.cursor = True
                if self.input_event_mode == 'right':
                    self.__cursor_right()
                elif self.input_event_mode == 'left':
                    self.__cursor_left()
                elif self.input_event_mode == 'shift-right':
                    self.__cursor_right_value()
                elif self.input_event_mode == 'shift-left':
                    self.__cursor_left_value()

    def __outline(self, ui):
        if self.active and self.is_outline:
            size = get_global_width(self.input_outline_size)
            color = self.input_outline_color
            x, y = get_global_size(self.input_x, self.input_y)

            pygame.draw.line(ui.surface_display, color, (x, y), (x + self.rect.width, y), width=size)
            pygame.draw.line(ui.surface_display, color, (x, y + self.rect.height),(x + self.rect.width, y + self.rect.height), width=size)
            pygame.draw.line(ui.surface_display, color, (x, y),(x, y + self.rect.height), width=size)
            pygame.draw.line(ui.surface_display, color, (x + self.rect.width, y),(x + self.rect.width, y + self.rect.height), width=size)

    def __add_value(self, text):
        self.__del_cursor()
        self.__add_text(text)

    def __add_text(self, text):
        for t in text:
            self.text_lst.insert(self.cursor_pos, t)
            self.cursor_pos += 1

    def __del_text(self):
        if self.text_lst and self.cursor_pos != 0:
            del self.text_lst[self.cursor_pos - 1]
            self.cursor_pos -= 1

    @staticmethod
    def __copy_text(text):
        pyperclip.copy(text)

    def __paste_text(self):
        if not self.cursor_value:
            self.__add_text(pyperclip.paste())
        else:
            self.__add_value(pyperclip.paste())

    def __cut_text(self, text):
        self.__del_cursor()
        self.__copy_text(text)

    def __cursor_right(self):
        if self.cursor_pos < len(self.text_lst):
            self.cursor_pos += 1
            self.cursor = True
            self.cursor_count = 0

    def __cursor_left(self):
        if self.cursor_pos != 0:
            self.cursor_pos -= 1
            self.cursor = True
            self.cursor_count = 0

    def __cursor_left_value(self):
        if self.cursor_pos > 0:
            if not self.cursor_value:
                self.cursor_value = [self.cursor_pos, self.cursor_pos - 1]
                self.cursor_pos -= 1
            elif self.cursor_value[1] > 0:
                self.cursor_pos -= 1
                self.cursor_value[1] -= 1

    def __cursor_right_value(self):
        if self.cursor_pos < len(self.text_lst):
            if not self.cursor_value:
                self.cursor_value = [self.cursor_pos, self.cursor_pos + 1]
                self.cursor_pos += 1
            elif self.cursor_value[1] < len(self.text_lst):
                self.cursor_pos += 1
                self.cursor_value[1] += 1

    def set_submit_func(self, func, *args, **kwargs):
        if self.enter_mode == EnterMode.Submit:
            self.submit_func = func
            self.args = args
            self.kwargs = kwargs

    def on_draw(self, ui):
        super().on_draw(ui)
        self.__mode()
        ui.surface_display.blit(self.box, self.rect)
        self.__cursor_value(ui)
        ui.surface_display.blit(self.text_surface, self.text_rect)

        self.__outline(ui)
        self.__cursor(ui)
        self.__del()
        self.__input()

    def on_input(self, event: pygame.event.Event):
        def active():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = True
                    self.cursor_value = None
                else:
                    self.active = False
        def _input():
            def text_input():
                match self.input_mode:
                    case InputMode.NumberInputMode:
                        if event.unicode in string.digits + ' _' and event.unicode != '':
                            if not self.cursor_value:
                                self.__add_text(event.text)
                            else:
                                self.__add_value(event.text)
                    case InputMode.TextInputMode:
                        if not self.cursor_value:
                            self.__add_text(event.text)
                        else:
                            self.__add_value(event.text)

            if self.active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.cursor_value:
                            self.__del_cursor()
                        else:
                            self.__del_text()
                            self.start_delete_count.start()
                    elif event.key == pygame.K_RETURN:
                        match self.enter_mode:
                            case EnterMode.Submit:
                                self.submit_func(*self.args, **self.kwargs)
                            case EnterMode.Text:
                                ...
                    elif event.mod & pygame.KMOD_CTRL:
                        if event.key == pygame.K_a:
                            end = len(self.text_lst)
                            self.cursor_value = [0, end]
                            self.cursor_pos = end
                        elif event.key == pygame.K_c:
                            if self.cursor_value and self.config["EnableCopying"]:
                                long = self.cursor_value[0] - self.cursor_value[1]

                                if long > 0:
                                    text = self.text_lst[self.cursor_value[1]:self.cursor_value[0]]
                                else:
                                    text = self.text_lst[self.cursor_value[0]:self.cursor_value[1]]
                                self.__copy_text(''.join(text))
                        elif event.key == pygame.K_v:
                            if self.config["EnablePasting"]:
                                self.__paste_text()
                        elif event.key == pygame.K_x:
                            if self.config["EnableCutting"]:
                                long = self.cursor_value[0] - self.cursor_value[1]

                                if long > 0:
                                    text = self.text_lst[self.cursor_value[1]:self.cursor_value[0]]
                                else:
                                    text = self.text_lst[self.cursor_value[0]:self.cursor_value[1]]
                                self.__cut_text(''.join(text))
                        elif event.key == pygame.K_LEFT:
                            self.cursor_pos = 0
                        elif event.key == pygame.K_RIGHT:
                            self.cursor_pos = len(self.text_lst)
                    elif event.mod & pygame.KMOD_SHIFT:
                        if event.key == pygame.K_LEFT:
                            self.__cursor_left_value()
                            self.input_event_mode = 'shift-left'
                            self.start_input_count.start()
                        elif event.key == pygame.K_RIGHT:
                            self.__cursor_right_value()
                            self.input_event_mode = 'shift-right'
                            self.start_input_count.start()
                    elif event.key == pygame.K_RIGHT:
                        if not self.cursor_value:
                            self.__cursor_right()
                            self.input_event_mode = 'right'
                            self.start_input_count.start()
                        else:
                            self.cursor_pos = self.cursor_value[int(self.cursor_value[1] > self.cursor_value[0])]
                            self.cursor_value = None
                    elif event.key == pygame.K_LEFT:
                        if not self.cursor_value:
                            self.__cursor_left()
                            self.input_event_mode = 'left'
                            self.start_input_count.start()
                        else:
                            self.cursor_pos = self.cursor_value[int(not self.cursor_value[1] > self.cursor_value[0])]
                            self.cursor_value = None
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        self.delete = False
                        self.start_delete_count.ret()
                    elif not event.mod and pygame.KMOD_SHIFT:
                        if event.key == pygame.K_LEFT:
                            self.input_event = False
                            self.input_event_mode = None
                            self.start_input_count.ret()
                        elif event.key == pygame.K_RIGHT:
                            self.input_event = False
                            self.input_event_mode = None
                            self.start_input_count.ret()
                    elif event.key == pygame.K_RIGHT:
                        self.input_event = False
                        self.input_event_mode = None
                        self.start_input_count.ret()
                    elif event.key == pygame.K_LEFT:
                        self.input_event = False
                        self.input_event_mode = None
                        self.start_input_count.ret()

                if event.type == pygame.TEXTINPUT:
                    text_input()
        active()
        _input()
