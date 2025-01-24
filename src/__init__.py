from src.Data import init

init()

from src.Libs.tool import *
from src.Page.Manager import PageManager
from src.Page.Manager.save_page import *
from src.Project.Page import ProjectPage
from src.REPL.Page import REPLPage
from src.Preform.surface import icon
from src.console import Display, Editor, Page
from src.window import *
import os
import pygame

class App:
    def __init__(self):
        pygame.init()
        os.environ["SDL_IME_SHOW_UI"] = "1"

        pygame.display.set_icon(icon)
        pygame.display.set_caption(f"{windows_title} {Editor.Version}")
        pygame.display.set_mode(windows_size, windows_state)

        set_page('manager', PageManager(['REPL', 'Project']))
        set_page('REPL', REPLPage())
        set_page('Project', ProjectPage())

        self.is_full_screen = Display.IsFullScreenState

        self.surface_display = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.page_manager = get_page('manager')
        self.REPL_page = get_page('REPL')
        self.Project_scene = get_page('Project')

    def full_screen(self):
        if self.is_full_screen:
            pygame.display.set_mode(Display.Size, 0)
        else:
            pygame.display.set_mode(Display.FullSize, pygame.FULLSCREEN)

        self.is_full_screen = not self.is_full_screen

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()
                if event.key == pygame.K_F11:
                    self.full_screen()
            self.page_manager.on_input(event)

    def update(self):
        self.clock.tick(60)

        self.page_manager.on_update()
        self.surface_display.fill(Display.FillColor)
        self.page_manager.on_draw()

        pygame.display.update()

    def run(self):
        self.page_manager.set_current_page(get_page(Page.Start))
        self.page_manager.on_enter()
        while True:
            self.handle_event()
            self.update()