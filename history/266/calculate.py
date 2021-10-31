from tkinter import *

# GUI
r = Tk()
r.wm_minsize(400, 160)
sne = Entry(r, width=8, justify="right", font=12)
sne.grid(row=0, column=0)


def giv(sne, v):
    """显示符号到显示屏"""
    sne.insert(END, v)


def GetClean():
    sne.delete(0, END)


def gr():
    """计算结果"""
    res = eval(sne.get())
    GetClean()
    sne.insert(0, str(res))


# 第二行
n1 = Button(r, text="1", width=8, height=2, command=lambda: giv(sne, "1"))
n1.grid(row=1, column=0)
n2 = Button(r, text="2", width=8, height=2, command=lambda: giv(sne, "2"))
n2.grid(row=1, column=1)
n3 = Button(r, text="3", width=8, height=2, command=lambda: giv(sne, "3"))
n3.grid(row=1, column=2)
n4 = Button(r, text="4", width=8, height=2, command=lambda: giv(sne, "4"))
n4.grid(row=1, column=3)
n5 = Button(r, text="5", width=8, height=2, command=lambda: giv(sne, "5"))
n5.grid(row=1, column=4)
# 第三行
n6 = Button(r, text="6", width=8, height=2, command=lambda: giv(sne, "6"))
n6.grid(row=2, column=0)
n7 = Button(r, text="7", width=8, height=2, command=lambda: giv(sne, "7"))
n7.grid(row=2, column=1)
n8 = Button(r, text="8", width=8, height=2, command=lambda: giv(sne, "8"))
n8.grid(row=2, column=2)
n9 = Button(r, text="9", width=8, height=2, command=lambda: giv(sne, "9"))
n9.grid(row=2, column=3)
n0 = Button(r, text="0", width=8, height=2, command=lambda: giv(sne, "0"))
n0.grid(row=2, column=4)
# 第四行
np = Button(r, text="+", width=8, height=2, command=lambda: giv(sne, "+"))
np.grid(row=3, column=0)
nm = Button(r, text="-", width=8, height=2, command=lambda: giv(sne, "-"))
nm.grid(row=3, column=1)
nr = Button(r, text="*", width=8, height=2, command=lambda: giv(sne, "*"))
nr.grid(row=3, column=2)
nd = Button(r, text="/", width=8, height=2, command=lambda: giv(sne, "/"))
nd.grid(row=3, column=3)
ne = Button(r, text="=", width=8, height=2, command=gr)
ne.grid(row=3, column=4)
# 第五行
ni = Button(r, text=".", width=8, height=2, command=lambda: giv(sne, "."))
ni.grid(row=4, column=0)
nc = Button(r, text="C", width=8, height=2, command=GetClean)
nc.grid(row=4, column=1)
# 运行这个窗口
r.mainloop()
