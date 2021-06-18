import numbers


def get16(num: int):
    string = ""
    while num > 0:
        oct16 = num % 16
        add = ""
        if oct16 == 15:
            add = 'F'
        elif oct16 == 14:
            add = 'E'
        elif oct16 == 13:
            add = 'D'
        elif oct16 == 12:
            add = 'C'
        elif oct16 == 11:
            add = 'B'
        elif oct16 == 10:
            add = 'A'
        elif 0 <= oct16 <= 9:
            add = str(oct16)
        string = add + string
        num = num // 16
    return string[-1] == 'B'


def get7(num: int):
    string = ""
    while num > 0:
        string = str(num % 7) + string
        num = num // 7
    return string[-1] == '6'

nums = []
for i in range(4221, 17523 + 1):
    if get16(i) or get7(i):
        nums.append(i)
print(len(nums))
print(sum(nums), min(nums))