import pygame as pg
import pickle
import os
class BigMap:
    LAND_MOUNTAIN = 0
    LAND_PLAIN = 1
    LAND_HOME = 2
    LAND_BOSS = 3
    WIDTH = 25
    HEIGHT = 25
    NODES_SAVE_PATH = 'Data/big_map/nodes.pickle'
    def __init__(self):
        self.Nodes = [[]]
        self.load_nodes()
        self.center = (BigMap.WIDTH//2, BigMap.HEIGHT//2)
        print(self.Nodes)

    def load_nodes(self):
        if os.path.exists(self.NODES_SAVE_PATH):
            with open('Data/big_map/nodes.pickle', 'rb') as f:
                self.Nodes = pickle.load(f)
        else:
            self.Nodes = [[self.LAND_PLAIN for i in range(BigMap.HEIGHT)] for j in range(BigMap.WIDTH)]
            self.Nodes[self.center[0]][self.center[1]] = self.LAND_HOME

    def save_nodes(self):
        with open('Data/big_map/nodes.pickle', 'wb') as f:
            pickle.dump(self.Nodes, f)

    def save(self):
        self.save_nodes()