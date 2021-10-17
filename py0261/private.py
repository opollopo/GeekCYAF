class Person(object):
    # 单下划线，表示被保护属性或方法，双下划线表示私有，子类也无法访问
    def __init__(self):
        __cqg = 50
        c = 500

    def __sysq(self, q):
        if self.__cqg is None:
            __cqg = 0
        self.__cqg += q

    def __h(self, jg):
        self.__cqg -= jg

    def gaosu(self):
        print("c")


wo = Person()
wo.gaosu()

