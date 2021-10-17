# 打地鼠
# 打到一次就胜利
# 没打到继续，一共有五次机会
import random


# 判断是否打到地鼠的函数
def foreach():
    m = random.randint(1, 5)
    h = int(input("请输入洞口编号对应的数字："))
    return m == h


for i in range(5):
    r = foreach()
    if r:
        print("Win")
        break
    else:
        print("继续")
        continue
else:
    print("Game Over!")


