# 多线程循环修改全局变量
import threading
import time

a = 1

def ma():
    global a
    a += 1

def pa():
    print(a)



t1 = threading.Thread(target=ma)
t1.start()
t0 = threading.Thread(target=pa)
t0.start()

#
# def ma():
#     global a
#     time.sleep(0.1)
#     for i in range(1000):
#         a += 1
#
#
# for i in range(50000):
#     t1 = threading.Thread(target=ma)
#     t1.start()
# print(a)
