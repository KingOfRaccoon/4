num = 49**8 + 7**24 - 749
string = ""
while num > 0:
    string = str(num % 7) + string
    num = num // 7
print(string.count('6'))