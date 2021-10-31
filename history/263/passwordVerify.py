# 密码验证
def pv(p):
    # 长度在8-16之间
    n = len(p)


# 不能有这种的111222，不能有字符连续出现3次
def pv3(p):
    for i in range(len(p) - 2):
        print(p[i], p[i + 1], p[i + 2])
        if p[i] == p[i + 1] == p[i + 2]:
            return False
    return True


while 1:
    r = input(":")
    if pv3(r):
        print("验证成功")
    else:
        print("验证失败")
