class B(object):
    __ins = None
    __f = True

    def __init__(self, p):
        if B.__f:
            print("初始化实例属性")
            self.price = p
            B.__f = False

    def __new__(cls, *args, **kwargs):
        print("开辟内存")
        if not cls.__ins:
            cls.__ins = object.__new__(cls)
        return cls.__ins


b = B(50)
b1 = B(30)
print("b的内存地址", id(b))
print("b1的内存地址", id(b1))
print(b.price)
