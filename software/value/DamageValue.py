class DamageValue:
    """描述伤害"""
    DAMAGE_PHYSICAL = 0
    DAMAGE_MAGIC = 1
    DAMAGE_REAL = 2

    def __init__(self, val: float, damage_type: int):
        """
        初始化
        :param val: 伤害值
        :param damage_type: 伤害类型
        """
        self.val = val
        self.type = damage_type
