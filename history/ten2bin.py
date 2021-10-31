
def d2m(m, n):
    if m == 1:
        if n == 0:
            return ""
        else:
            return "0"*n
    r = ""
    t = divmod(n, m)
    b = t[1]
    s = t[0]
    r += str(b)
    while s > 0:
        t = divmod(s, m)
        b = t[1]
        s = t[0]
        r += str(b)
    return r[::-1]


p = int(input("请输入一个进制："))
num = int(input("请输入一个数量(正整数)："))
print('数量{0}对应的{1}进制的数是{2}'.format(num,p,d2m(p, num)))


