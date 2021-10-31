# 抽奖程序, random
import random

# 模拟10000次抽奖，查看抽奖后各等级奖品的个数
l1, l2, l3 = 0, 0, 0
for i in range(10000):
    num = random.random()
    if 0 <= num < 0.08:
        l1 += 1
    elif 0.08 <= num < 0.3:
        l2 += 1
    else:
        l3 += 1
print("一等奖%d个,二等奖%d个,三等奖%d个" % (l1, l2, l3))
