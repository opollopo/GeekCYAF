# t = open("t1.txt", "a")
# t.write("9")
# t.close()

y = [4, 5, 6, 3, 2, 1]
n = len(y)
for i in range(n-1):
    for j in range(n-i-1):
        if y[j] > y[j+1]:
            y[j], y[j+1] = y[j+1], y[j]
    print(y)
