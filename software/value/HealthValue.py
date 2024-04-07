class HealthValue:
    def __init__(self, health, h_max=-1):
        """
        初始化生命值
        :param health: 初始生命值
        :param health: 生命值上限，不填则为初始生命值
        """
        self.val = health
        self.val_max = h_max if h_max != -1 else health
