class PowerAdapter(object):
    def __init__(self):
        shuruV = 220
        shuruA = 0.5
        shuchuV = 5
        shuchuA = 2


    def transfer(self):
        pass


class Phone(object):
    pass
    # def __init__(self):
    #     self.shuruV = 220
    #     self.shuruA = 0.5
    #     self.version = "miui"
    #
    # def charge(self, adapter):
    #     print(self.shuruV)
    #     self.act1()
    #     adapter.transfer()
    #
    # def act1(self):
    #     pass
a = PowerAdapter()
p = Phone()
p.charge(a)


class Phone12E128(Phone):
    rdb = 8
    rwd = 128

    def __init__(self, owner):
        self.owner = owner


p12 = Phone12E128("Lucy")
print(p12.owner, p12.rdb, p12.rwd)

