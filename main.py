import pygame as pg
import sys
import logging
from software.component.BigMap import BigMap
from software.component.StartPage import StartPage
from software.value.StaticVal import *


class Main:
    CLOCK = pg.time.Clock()

    def __init__(self):
        pg.init()
        pg.display.set_caption(Screen.TITTLE)
        pg.display.set_icon(pg.image.load("the_sand.ico"))

        self.start_page = StartPage()
        self.big_map = BigMap()
        self.show_UI = UI.START

    def show(self):
        Screen.SCREEN.fill(Screen.COLOR)
        if self.show_UI == UI.START:
            self.start_page.show(Screen.SCREEN)
        elif self.show_UI == UI.BIG_MAP:
            self.big_map.show(Screen.SCREEN)

    def run_page(self):
        if self.show_UI == UI.START:
            self.start_page.run()

    def run(self):
        pg.mixer.music.load("Music/[沙中之火]生息.mp3")
        pg.mixer.music.play()
        while True:
            self.run_page()
            self.show()
            pg.display.flip()
            self.set_event()
            Main.CLOCK.tick(Screen.FPS)

    def set_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.save()
                sys.exit()
            elif event.type == Event.CHANGE_PAGE:
                self.show_UI = event.new_UI
                logging.info(f"显示界面变更为{event.new_UI}")
            self.start_page.set_event(event)

    def save(self):
        self.big_map.save()


if __name__ == '__main__':
    m = Main()
    m.run()
