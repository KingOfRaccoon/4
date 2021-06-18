for x in range(1, 1001):
    cope = x
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 7)
        x = x // 7
    if a == 4 and b == 30:
        print(cope)