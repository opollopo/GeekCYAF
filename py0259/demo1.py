class Person(object):
    dna = 23
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __del__(self):
        print("执行了删除")

    def __str__(self):
        return str(self.age) + self.name

    def __call__(self, *args, **kwargs):
        print('2')

    def run(self):
        print("跑")

    @classmethod
    def extent(cls):
        cls.dna = 20


    @staticmethod
    def time():
        print()




p = Person("A",18)
p.run()
a = 5
print(isinstance(a, int))
p()
help(Person)
id(p)


def f(p):
    print(p.name)
    p.run()




class Dog(object):
    def __init__(self):
        self.name = "旺财"

    def run(self):
        print("跑")

d = Dog()
f(d)
f(p)

# p = Person("Python", 14)
# print(p)
# del p
class Home(object):
    def __init__(self, a):
        self.area = a
        self.containsItem = []

    def __str__(self):
        msg = "当前房间可用面积" + str(self.area)
        if len(self.containsItem) > 0:
            msg += "容纳的物品有："
        for i in self.containsItem:
            msg += str(i) + ","
        return msg

    def put_item(self, item):
        if item.area > self.area:
            print("放不下了")
        else:
            self.containsItem.append(item)
            self.area -= item.area
            print("摆放成功")


class Goods(object):
    pass


class CommunityHome(Home, Goods):
    pass


c = CommunityHome(200)
print(c)


class Bed(object):
    def __init__(self, a):
        self.area = a

    def __str__(self):
        return "一张床"


#
# h = Home(100)
# print(h)
# b = Bed(4.5)
# h.put_item(b)
# print(h)


class Master(object):
    def __init__(self):
        self.kong_fu = "古法煎饼果子配方"

    def make_cake(self):
        print("按照%s制作了煎饼果子" % self.kong_fu)


class School(object):
    def __init__(self):
        self.kong_fu = "现代方法煎饼果子配方"

    def make_cake(self):
        print("按照%s制作了煎饼果子" % self.kong_fu)


class Prentice(Master, School):
    pass

damao = Prentice()
damao.make_cake()