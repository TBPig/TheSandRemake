import pygame as pg
import sys
from software.component.BigMap import BigMap
from software.component.StartPage import StartPage


class Main:
    SCREEN_MODE = (1200, 600)
    SCREEN_COLOR = (192, 212, 32)
    SCREEN_TITTLE = "The Sand"
    SCREEN = pg.display.set_mode(SCREEN_MODE)
    FPS = 30
    CLOCK = pg.time.Clock()
    def __init__(self):
        pg.init()
        Main.SCREEN.fill(Main.SCREEN_COLOR)
        pg.display.set_caption(Main.SCREEN_TITTLE)
        pg.display.set_icon(pg.image.load("the_sand.ico"))

        self.start_page = StartPage()
        self.big_map = BigMap()
        self.focus_point = pg.Rect(0, 0, 0, 0)

    def run(self):
        pg.mixer.music.load("Music/[沙中之火]生息.mp3")
        pg.mixer.music.play()
        while True:
            self.start_page.show(Main.SCREEN)
            pg.display.flip()
            self.disposal_event()
            Main.CLOCK.tick(Main.FPS)

    def disposal_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.save()
                sys.exit()
            self.start_page.set_event(event)

    def save(self):
        self.big_map.save()


if __name__ == '__main__':
    m = Main()
    m.run()
