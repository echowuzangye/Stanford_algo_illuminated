import profile


with open("2sum.txt") as file:
    content = file.readlines()
    nums = [int(line) for line in content]
    num = sorted(nums)


# set two pointers
i, j = 0, len(num) - 1
seen = set()
count = 0

while i < j:
    if num[i] + num[j] < -10000:
        i += 1
    elif num[i] + num[j] > 10000:
        j -= 1
    else:
        two_sum = num[i] + num[j]
        if two_sum not in seen:
            seen.add(two_sum)
            count += 1
        i += 1

profile.run('print(count);print()')






