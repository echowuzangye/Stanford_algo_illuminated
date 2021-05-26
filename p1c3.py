
# 1. first write merge; 2. write merge-sort
# 3. Programming Problem 3.5: Counting inversions

def merge_lst(l1, l2):
    final_lst = []
    i, j, k = 0, 0, 0
    for k in range(len(l1)+len(l2)):
        if i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                final_lst.append(l1[i])
                i, k = i+1, k+1
            else:
                final_lst.append(l2[j])
                j, k = j+1, k+1
        elif i == len(l1):
            final_lst.extend(l2[j:])
            # need to use extend instead of append, otherwise final list will be [1, 2, 3, 4, 5, [8]]
            return final_lst
        else:
            final_lst.extend(l1[i:])
            return final_lst


# print(merge_lst([1,3,5],[2,4,8]))
# can I make it better?


def merge_sort(l):
    assert type(l) is list
    if len(l) == 1:
        return l
    else:
        n = len(l)
        return merge_lst(merge_sort(l[:(n//2)]), merge_sort(l[(n//2):]))

# print(merge_sort([1,5,2,4,9,7,8]))


def merge_count_split(l1, l2, split_inv):
    """Merge two sorted array, output are one sorted array and split count"""
    final_lst = []
    i, j, k = 0, 0, 0
    for k in range(len(l1) + len(l2)):
        if i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                final_lst.append(l1[i])
                i, k = i + 1, k + 1
            else:
                final_lst.append(l2[j])
                j, k, split_inv = j + 1, k + 1, split_inv+len(l1)-i
        elif i == len(l1):
            final_lst.extend(l2[j:])
            # need to use extend instead of append, otherwise final list will be [1, 2, 3, 4, 5, [8]]
            return final_lst, split_inv
        else:
            final_lst.extend(l1[i:])
            return final_lst, split_inv


# a, b = merge_count_split([1, 3, 5], [2, 4, 6], 0)
# print(a,b)

def count_inv(l):
    assert type(l) is list

    def helper(l, split_inv):
        if len(l) == 1:
            return l, split_inv
        else:
            n = len(l)
            a1, b1 = helper(l[0:n//2], split_inv)
            a2, b2 = helper(l[n//2:], split_inv)
            return merge_count_split(a1,a2,b1+b2)
    return helper(l, 0)

#1. base test case
# a, b = count_inv([9,8,7,6,5,4,3,2,1])
# print(a, b)

#2. test case 28 inversions
# a, b = count_inv([54044, 14108,79294,29649,25260,60660, 2995, 53777, 49689, 9083])
# print(a, b)

#3. Challenge data set: This file contains all of the integers between 1 and 100,000 (inclusive) in some order,
# with no integer repeated. The ith row of the file indicates the ith entry of an array. How many inversions does
# this array have? (Obviously, to get the most out of this assignment, you should implement the fast divide-and-conquer
# algorithm from Section 3.2, rather than brute-force search.)

# read the code txt file and replace "\n" with ","

# integer_lst =[]
# with open('p1c3_IntegerArray.txt') as file:
#     contents = file.read()
#     contents = contents.split('\n')
#     contents.pop()
#     # remove the last empty item ''
#     for item in contents:
#         integer_lst.append(int(item))
#
# a, b = count_inv(integer_lst)
# print(a, b)

# Problem 3.2
def unimodal(l):
    if len(l) == 1:
        return l[0]
    else:
        n = len(l)
        if l[n//2-1] > l[n//2]:
            return unimodal(l[:n//2])
        else:
            return unimodal(l[n//2:])

# Problem 3.3
def index_equal(l):
    """ find  whether or not there is an index i such that A[i] = i, assuming one or none"""
    def helper(l, k):
        n = len(l)
        if n == 1 and l[0] != k:
            return "doesn't exist"
        if l[n//2 - 1] > n//2 -1 + k:
            return helper(l[:n//2], k)
        elif l[n//2 -1] == n//2 -1 + k:
            return l[n//2 - 1]
        else:
            return helper(l[n//2:], k+n//2)
    return helper(l, 0)

print(index_equal([-1,0,2,4,5]))

# Problem 3.4
#similar to MIT 6.006 Lecture 1 2D peak
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec01.pdf
# • Pick middle column j = m/2
# • Find global minimum on column j at (i, j)
# • Compare (i, j − 1),(i, j),(i, j + 1)
# • Pick left columns if (i, j − 1) < (i, j)
# • Similarly for right
# • (i, j) is a local minimum if neither condition holds
# • Solve the new problem with half the number of columns.
# • When you have a single column, find global minimum and you‘re done.
#  Takes 0(nlogn) time