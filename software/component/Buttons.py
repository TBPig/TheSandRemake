import pygame as pg
from software.value.StaticVal import Color


def get_center_rect(rect1: pg.Rect, rect2: pg.Rect):
    rect2.x = rect1.centerx - rect2.width / 2
    rect2.y = rect1.centery - rect2.height / 2
    return rect2


class Button:
    FONT_PATH = pg.font.match_font('SimHei')  # 显示中文的设置和字体，及路径

    def __init__(self, text, text_size=30, rect: pg.Rect = pg.Rect(100, 100, 100, 100)):
        self.rect = rect
        self.color = Color.GREY
        self.text_color = Color.WHITE
        self.font = pg.font.Font(Button.FONT_PATH, text_size)
        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = get_center_rect(self.rect, self.text.get_rect())
        self.shadow = (64, 64, 64)
        self.press_flag = False
        self.agree_flag = False

    def show(self, screen: pg.Surface):
        # 绘制按钮
        pg.draw.rect(screen, self.color, self.rect)
        if self.press_flag:
            pg.draw.rect(screen, self.shadow, self.rect)
        screen.blit(self.text, self.text_rect)

    def set_event(self, event):
        # 监听事件
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # 在这里执行按钮点击后的操作
                self.press_flag = True
        if event.type == pg.MOUSEBUTTONUP:
            self.press_flag = False
            if self.rect.collidepoint(event.pos):
                # 在这里执行按钮点击后的操作
                self.agree_flag = True

    def set_color(self, color: tuple):
        self.color = color

    def set_shadow_color(self, color: tuple):
        self.shadow = color
