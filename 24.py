with open("24.txt") as file:
    data = file.read()
    print(data.count('X'*10) + data.count('Y'*7) + data.count('Z' * 5))
    print('X'*10)
    print('Y'*7)
    print('Z' * 5)