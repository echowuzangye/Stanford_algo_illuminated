import heapq


with open("Median.txt") as file:
    content = file.readlines()
    input_l = [int(item) for item in content]
    print("data loaded")


h1, h2 = [], []
# initialization, first two items; h1 is a reversed min-heap, with every item * -1
if input_l[0] < input_l[1]:
    heapq.heappush(h1, input_l[0]*(-1))
    heapq.heappush(h2, input_l[1])
else:
    heapq.heappush(h1, input_l[1]*(-1))
    heapq.heappush(h2, input_l[0])


def find_max(q):
    """ for h1"""
    return q[0]*(-1)


def find_min(q):
    """ for h2"""
    return q[0]


def heap_balance(q1, q2):
    if abs(len(q1) - len(q2)) < 2:
        return q1, q2
    elif len(q1) > len(q2):
        heapq.heappush(q2, heapq.heappop(q1)*(-1))
    else:
        heapq.heappush(q1, heapq.heappop(q2)*(-1))
    return q1, q2


m_sum = input_l[0] + find_max(h1)
print(m_sum)

# # from third item
for i in range(2, len(input_l)):
    if input_l[i] > find_max(h1):
        heapq.heappush(h2, input_l[i])
    else:
        heapq.heappush(h1, input_l[i]*(-1))
    h1, h2 = heap_balance(h1, h2)
    if len(h1) == len(h2) or len(h1) > len(h2):
        m_sum += find_max(h1)
    else:
        m_sum += find_min(h2)

print(m_sum)


