def max_heapify(A, i):
    """correct a single violation of the heap property"""
    left = 2*i + 1
    right = 2*i + 2
    if i <= len(A) - 1 and A[i] < A[left]:
        largest = left
    else:
        largest = i
    if i <= len(A) - 1 and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
    return A


# print(max_heapify([16,14,10,2,7,9,3,8,4,1], 3))


def build_max_heap(A):
    """produce a max-heap from an unordered array"""
    i = int((len(A)-2)//2)
    while i >= 0:
        max_heapify(A, i)
        i -= 1
    return A
print(build_max_heap([3,2,1,7,9,4,8]))


