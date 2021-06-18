string = '1' * 84
while '11111' in string or '888' in string:
    if '11111' in string:
        string = string.replace('11111', '88', 1)
    else:
        string = string.replace('888', '88', 1)
    print(string)