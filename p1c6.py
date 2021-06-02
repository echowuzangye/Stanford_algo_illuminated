import random


# Problem 6.5 Implement RSelect Algorithm
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


def random_select(array, n):

    def helper(a, l, r, n):
        if l == r:
            return a[l]
        else:
            i = choose_pivot(a, 3, l, r)
            a = swap_position(a, l, i)
            j = partition(a, l, r)
            if j == n-1:
                return a[j]
            elif j > n-1:
                return helper(a, l, j - 1, n)
            else:
                return helper(a, j + 1, r, n)
    return helper(array, 0, len(array) - 1, n)


test_1 = []
with open('problem6.5test1.txt') as file:
    contents = file.read()
    contents = contents.split('\n')
    contents.pop()
    # remove the last empty item ''
    for item in contents:
        test_1.append(int(item))


# print(random_select(test_1, 5))

test_2 = []
with open('problem6.5test2.txt') as file:
    contents = file.read()
    contents = contents.split('\n')
    contents.pop()
    # remove the last empty item ''
    for item in contents:
        test_2.append(int(item))

print(random_select(test_2, 50))


# Problem 6.3
