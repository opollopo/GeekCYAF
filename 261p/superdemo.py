class Father(object):
    _secret = 80
    h1 = 180

    def __buyPlane(self):
        pass

    def server(self, guke):
        print("提供食物")


class Mom(object):
    h = 170



class Child(Father, Mom):
    def act(self):
        print("儿子的身高随父亲",super().h)
        super(Child, self).server()

class GrandChild(Child):
    pass

c = Child()
c.act()
print(locals())
print(globals())
