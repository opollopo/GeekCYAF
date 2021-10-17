class House(object):
    win = True
    door = True

    def __init__(self, n, m):
        self.win_num = n
        self.door_num = m

    def zhuangren(self, shuliang):
        House.win
        pass

    @classmethod
    def zhefengdangyu(cls):
        return True

    @staticmethod
    def fun1(zone):
        return 1


p = House(2, 1)
p.zhuangren(5)

p1 = House(2, 1)
p1.zhuangren(6)
House.zhefengdangyu()
p1.fun1("beijing")
House.fun1("沈阳")
p1.zhefengdangyu()
