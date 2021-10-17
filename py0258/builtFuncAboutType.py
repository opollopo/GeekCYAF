class Student(object):
    """学生类"""
    xueximudi = "不清楚"

    def __init__(self,name,age):
        self.name = name
        self.age = age


    @classmethod
    def watch(cls):
        pass

    def read(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


# isinstance 判断某个对象是否是某个已知类型
a = 5


# print(isinstance(a, int))
# print(isinstance(a, Student))
# print(isinstance(int, type))
# print(isinstance(False, bool))
# print(isinstance(False, int))
# callable 判断是否可被调用,函数，类,lambda函数,具有__call__这个实例方法的实例也能被调用

def add(x, y):
    """返回两个数的和"""
    return x + y


# add(1, 1)
# p = Student()
# y = lambda x, y: x + y
# y(1, 2)
# print(callable(add))
# print(callable(Student))
# print(callable(lambda x, y: x + y))
# print(callable(p))

# help 查看函数说明
# help(Student)

# id()获取对象内存地址,不可变类型，数字，字符串，元组
a = 5
c = a
b = 5
# name1 = "张三"
# name2 = "张三"
# # print(id(add))
print("a的内存地址", id(a))
print("c的内存地址", id(c))
print("b的内存地址", id(b))
# print("name1的内存地址", id(name1))
# print("name2的内存地址", id(name2))

# vars(object) 返回这个对象的属性值和属性值字点
# print(vars(int))
