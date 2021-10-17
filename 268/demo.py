# join
import threading
import time

if __name__ == '__main__':
    print("开始")

    def dance():
        time.sleep(1)
        print("跳舞")
    t = threading.Thread(target=dance)
    t.start()
    t.join()
    print("结束")

