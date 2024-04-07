import pygame as pg
from software.value.StaticVal import *
from software.component.Page import Page
import pickle
import os


class BigMap(Page):
    WIDTH = 25
    HEIGHT = 25
    NODES_SAVE_PATH = 'Data/big_map/nodes.pickle'
    NODE_SIZE = (64, 64)
    IMG_HOME = pg.transform.scale(pg.image.load("Pic/家园节点.png"), NODE_SIZE)
    IMG_MOUNTAIN = pg.transform.scale(pg.image.load("Pic/山地节点.png"), NODE_SIZE)
    IMG_PLAIN = pg.transform.scale(pg.image.load("Pic/平原节点.png"), NODE_SIZE)
    IMG_DIC = {Land.HOME: IMG_HOME, Land.MOUNTAIN: IMG_MOUNTAIN, Land.PLAIN: IMG_PLAIN}

    def __init__(self):
        self.nodes = [[]]
        self.load_nodes()
        self.center = (BigMap.WIDTH * BigMap.NODE_SIZE[0] // 2, BigMap.HEIGHT * BigMap.NODE_SIZE[1] // 2)
        self.focus = pg.Rect(0, 0, *Screen.MODE)
        self.focus.center = self.center

    def show(self, screen):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                img = BigMap.IMG_DIC[self.nodes[x][y]]
                rect = pg.Rect(x * BigMap.NODE_SIZE[0], y * BigMap.NODE_SIZE[1], 0, 0)
                screen.blit(img, (rect[0] - self.focus[0], rect[1] - self.focus[1]))

    def load_nodes(self):
        if os.path.exists(self.NODES_SAVE_PATH):
            with open('Data/big_map/nodes.pickle', 'rb') as f:
                self.nodes = pickle.load(f)
        else:
            self.nodes = [[Land.PLAIN for i in range(BigMap.HEIGHT)] for j in range(BigMap.WIDTH)]
            self.nodes[BigMap.HEIGHT//2][BigMap.WIDTH//2] = Land.HOME

    def save_nodes(self):
        with open('Data/big_map/nodes.pickle', 'wb') as f:
            pickle.dump(self.nodes, f)

    def save(self):
        self.save_nodes()
