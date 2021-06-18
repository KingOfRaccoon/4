def check(num: int):
    return sum([int(x) for x in str(num)[:3]]) == sum([int(x) for x in str(num)[-3:]])

nums = []
for i in range(100000, 999999 + 1):
    if check(i):
        nums.append(i)
print(sum(nums))
print(nums)