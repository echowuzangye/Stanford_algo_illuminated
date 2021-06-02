import random


# Problem 5.6
def choose_pivot(a, n, l, r):
    """n==1, pick the first element;
       n==2, pick the last element;
       n==3, pick a random element;
       n==4, pick the median-of-three element"""
    if n == 1:
        return l
    elif n == 2:
        return r
    elif n == 3:
        return random.randint(l, r)
    else:
        mid_index = (r - l) // 2 + l
        median_of_three = [a[l], a[r], a[mid_index]]
        min_element, max_element = min(median_of_three), max(median_of_three)
        if a[l] != min_element and a[l] != max_element:
            return l
        elif a[r] != min_element and a[r] != max_element:
            return r
        else:
            return mid_index
        # can this be simplified?


def partition(a, l, r):
    p, i = a[l], l + 1
    for j in range(l + 1, r + 1):
        if a[j] < p:
            swap_position(a, j, i)
            i += 1
    swap_position(a, l, i - 1)
    return i - 1


def swap_position(a, pos1, pos2):
    a[pos1], a[pos2] = a[pos2], a[pos1]
    return a


def quicksort(array):
    count_comparison = 0

    def helper(a, l, r):
        nonlocal count_comparison
        if l >= r:
            return count_comparison//2
        else:
            i = choose_pivot(a, 3, l, r)
            a = swap_position(a, l, i)
            j = partition(a, l, r)
            count_comparison += r - l
            helper(a, l, j - 1)
            helper(a, j + 1, r)
        return count_comparison

    return helper(array, 0, len(array) - 1)


test_1 = []
with open('problem5.6test1.txt') as file:
    contents = file.read()
    contents = contents.split('\n')
    contents.pop()
    # remove the last empty item ''
    for item in contents:
        test_1.append(int(item))

# print(quicksort(test_1))

test_2 = []
with open('problem5.6test2.txt') as file:
    contents = file.read()
    contents = contents.split('\n')
    contents.pop()
    # remove the last empty item ''
    for item in contents:
        test_2.append(int(item))

# print(quicksort(test_2))

test_3 = []
with open('problem5.6.txt') as file:
    contents = file.read()
    contents = contents.split('\n')
    contents.pop()
    # remove the last empty item ''
    for item in contents:
        test_3.append(int(item))

print(quicksort(test_3))
# first element as pivot:162085
# last element as pivot:164123
# median-three element as pivot:138382
# random pivot:between median and first
