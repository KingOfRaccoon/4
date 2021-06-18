with open("26.txt") as file:
    data = [int(x) for x in file.read().split()]
    size = data.pop(0)
    k = data.pop(0)
    data.sort(reverse=True)
    print(data)
    print(sum(data[:61]))
