# new方法，用处：在内存条上开辟一个内存空间，
# init 与new谁先执行

class A(object):
    def __init__(self, p):
        self.price = p
        print("初始化实例属性")

    def __new__(cls, *args, **kwargs):
        print("这是new方法, 开辟了一个内存空间")
        return object.__new__(cls)


a = A(50)
# print("a.price=", a.price)
b = A(30)
print("a的内存地址", id(a))
print("b的内存地址", id(b))
a.price
b.price
