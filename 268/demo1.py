# join
import threading
import time

if __name__ == '__main__':
    print("开始")
    balance = 0

    def shoukuan():
        time.sleep(1)
        global balance
        balance += 5

    tl = []
    for i in range(100):
        tl.append(threading.Thread(target=shoukuan))
        tl[i].start()
    for j in range(100):
        tl[j].join()

    print("结束,一共收入：%f"%balance)

