def getDel31(data: list):
    dels = []
    for i in range(len(data)):
        if data[i] % 31 == 0:
            dels.append([i, data[i]])
    return dels

with open("27-A.txt") as file:
    data = [int(x) for x in file.read().split()]
    size = data.pop(0)
    dels = getDel31(data)
    data_and_index = [[x, data[x]] for x in range(len(data))]
    print(dels)
    sums = []
    for i in dels:
        index = i[0]
        num = i[1]
        for j in data_and_index:
            index_j = j[0]
            num_j = j[1]
            if abs(index - index_j) >= 4 and num_j != num:
                sums.append(num * num_j)
    print(len(sums))