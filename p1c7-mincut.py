import random

# too slow, need improvement
def load_data():
    """create a adjacent linked list based on the original text file
    it looks like
    [[[0], [[1], [2], [3]]], [[1], [[0], [3]]], [[2], [[0], [3]]], [[3], [[1], [0], [2]]]]"""
    adj_all_list = []
    with open('kargerMinCut.txt') as file:
        contents = file.read()
        contents = contents.split('\n')
        contents.pop()
        # remove the last empty item ''
        for item in contents:
            contents_2 = item.split('\t')
            contents_2.pop()
            adj_list = [[], []]
            for i in range(0, len(contents_2)):
                if i == 0:
                    adj_list[0].append(int(contents_2[0]))
                else:
                    adj_list[1].append([int(contents_2[i])])
            adj_all_list.append(adj_list)
    return adj_all_list


def remove_all(l, item):
    """remove all occurrence of an item from a list"""
    l = [i for i in l if i != item]
    return l

def contraction(l):
    """pick two vertices,  combine nodes ver_1 and ver_2, update adj_all_list to remove the ver_2 nodes"""
    i = random.randint(0, len(l) - 1)
    j = random.randint(0, len(l[i][1]) - 1)
    ver_1, ver_2 = l[i][0], l[i][1][j]
    ver_2_lst = [a for a in l if a[0] == ver_2][0]
    l[i][1].extend(ver_2_lst[1])
    l[i][1] = remove_all(l[i][1], ver_1)
    l[i][1] = remove_all(l[i][1], ver_2)
    l.remove(ver_2_lst)
    new_combined_ver = ver_1 + ver_2
    # use + instead of append, append will change ver_1 since they are pointing to the same list
    replace(l, ver_1, ver_2,  new_combined_ver)


def contraction_min_cut(l):
    """ use contraction algorithm to solve the minimum cut problem. l is the adjacent list,
    n is the number of times we want to run the algorithm.
    """
    while len(l) != 2:
        contraction(l)
    min_cut = len(l[0][1])
    return min_cut


def replace(l, ver_1, ver_2,  new_combined_ver):
    """Remove ver_1 and ver_2 from all vertices' edges and replace them with new_combined_ver"""
    for item in l:
        if item[0] == ver_1:
            item[0] = new_combined_ver
        for i in range(0,len(item[1])):
            if item[1][i] == ver_1 or item[1][i] == ver_2:
                item[1][i] = new_combined_ver


""" for good result, run at least n^2ln(n) times to have pr[all trials fail]<= 1/n"""
min_cut_lst = []
for n in range(0, int(200)):
    l = load_data()
    min_cut_lst.append(contraction_min_cut(l))
print(min(min_cut_lst))





