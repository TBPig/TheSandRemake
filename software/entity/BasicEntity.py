import pygame as pg
from software.value.HealthValue import HealthValue


class BasicEntity:
    def __init__(self):
        self.health = HealthValue(1000)     # 生命值
        self.Atk = 100  # 攻击力
        self.Def = 0    # 防御力
        self.Mr = 0     # 法抗
        self.speed = 0  # 移速
