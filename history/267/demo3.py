import threading
num = 0

def test():
    lo.acquire()
    global num
    for i in range(10000000):
        num -= 100
        num += 100
    lo.release()


if __name__ == '__main__':
    lo = threading.Lock()
    t1 = threading.Thread(target=test)
    t2 = threading.Thread(target=test)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num=", num)
