def huiwen(s):
    return s == s[::-1]


# print(huiwen("aba"))
# lambda s:s == s[::-1]


def pingfang(x):
    return x ** 2


t = list(map(lambda x: x ** 2, range(1, 101)))
print(t)

listinfo = [133, 88, 24, 33, 232, 44, 11, 44]


def func(o):
    return list(filter(lambda x: x < 100 and x % 2 == 0, o))


print(func(listinfo))


li = [3, 25, 1, 2, 55, 16]
i = 0
try:
    while i <= len(li):
        print(li[i])
        i += 1
except Exception as e:
    print(1)
else:
    print(2)
finally:
    print(3)
