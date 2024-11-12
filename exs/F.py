def F(x):
    total = 0
    while x > 0:
        total = total + x
        x = x // 10
    return total

num = 404
print(F(num))