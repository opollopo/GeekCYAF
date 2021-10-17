import threading
import time


def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(5)


def dance():
    for i in range(4):
        print("跳舞")
        time.sleep(10)


t1 = threading.Thread(target=sing)
t1.start()
t2 = threading.Thread(target=dance)
t2.start()

t1 = threading.Thread(target=sing)
t1.start()
t2 = threading.Thread(target=dance)
t2.start()

t1 = threading.Thread(target=sing)
t1.start()
t2 = threading.Thread(target=dance)
t2.start()

t1 = threading.Thread(target=sing)
t1.start()
t2 = threading.Thread(target=dance)
t2.start()
#
# for i in range(1000):
#     t = threading.Thread(target=dance)
#     t.start()
