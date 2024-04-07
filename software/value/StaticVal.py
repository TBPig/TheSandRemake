import pygame as pg
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)


class Land:
    MOUNTAIN = 0
    PLAIN = 1
    HOME = 2
    BOSS = 3


class UI:
    START = 0
    BIG_MAP = 1
    SETTING = 2


class Event:
    CHANGE_PAGE = 0


class Screen:
    MODE = (1200, 600)
    COLOR = (192, 212, 32)
    TITTLE = "The Sand"
    SCREEN = pg.display.set_mode(MODE)
    FPS = 30
