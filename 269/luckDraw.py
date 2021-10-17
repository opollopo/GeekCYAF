import threading
from tkinter import *
import time

r = Tk()
r.title("轮盘")
r.wm_minsize(290, 370)
b1 = Button(r, text="蓝牙耳机", bg="red")
b1.place(x=20, y=20, width=70, height=70)
b2 = Button(r, text="祝你好运", bg="white")
b2.place(x=110, y=20, width=70, height=70)
b3 = Button(r, text="抱枕", bg="white")
b3.place(x=200, y=20, width=70, height=70)

b4 = Button(r, text="谢谢", bg="white")
b4.place(x=20, y=110, width=70, height=70)

b6 = Button(r, text="保温杯", bg="white")
b6.place(x=200, y=110, width=70, height=70)

b7 = Button(r, text="飞行汽车", bg="white")
b7.place(x=20, y=200, width=70, height=70)
b8 = Button(r, text="钓鱼岛", bg="white")
b8.place(x=110, y=200, width=70, height=70)
b9 = Button(r, text="飞行能力", bg="white")
b9.place(x=200, y=200, width=70, height=70)

btn_list = [b1, b2, b3, b4, b6, b7, b8, b9]
is_loop = False
is_run = False


def round_c():
    if is_loop:
        return
    j = 0
    while 1:
        time.sleep(0.1)
        for i in btn_list:
            i['bg'] = 'white'
        btn_list[j]['bg'] = 'red'
        j += 1
        if j >= 8:
            j = 0
        if is_run:
            continue
        else:
            break


def start_round():
    global is_loop, is_run
    t = threading.Thread(target=round_c)
    t.start()
    is_loop = True
    is_run = True


# define  定义 ，def用于定义一个函数
def stop():
    global is_loop, is_run
    is_loop = False
    is_run = False


sbtn = Button(r, text="开始", command=start_round)
sbtn.place(x=70, y=300, width=60, height=40)

ebtn = Button(r, text="结束", command=stop)
ebtn.place(x=160, y=300, width=60, height=40)

r.mainloop()
