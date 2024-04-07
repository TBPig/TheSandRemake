import pygame as pg
from software.component.Buttons import Button
from software.component.Page import Page
from software.value.StaticVal import *


class StartPage(Page):
    def __init__(self):
        self.start_button = Button("start")

    def run(self):
        if self.start_button.is_agree:
            pg.event.post(pg.event.Event(Event.CHANGE_PAGE, new_UI=UI.BIG_MAP))

    def show(self, screen):
        self.start_button.show(screen)

    def set_event(self, event):
        self.start_button.set_event(event)
