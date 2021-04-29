# Justin Ventura

import sys
from itertools import combinations

def has_edge(e, subset):
    temp = []
    for s in subset:
        temp += e[s]

    for i in subset:
        if i in temp:
            return True
    return False

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')
    vertices = lines[0].split(' ')

    edges = {}
    for v in vertices:
        edges[v] = []

    match = len(vertices) / 2

    for i in range(1, len(lines)-1):
        u, v = lines[i].split(' ')
        edges[u].append(v)
        edges[v].append(u)

    subsets = []
    for i in range(1, len(vertices)):
        subsets.append([c for c in combinations(vertices, i)])

    new_sets = []
    for leng in subsets:
            for s in leng:
                if has_edge(edges, s) == False:
                    new_sets.append(s)

    newer_set = []
    for ns in new_sets:
        if len(ns) == match:
            newer_set.append(ns)

    temp = []
    for i, x in enumerate(newer_set):
        for j, y in enumerate(newer_set):
            if i!=j:
                temp.append(x+y)

    temp2=[]
    for t in temp:
        for t_i in t:
            if t not in temp2:
                temp2.append(t_i)
            else:
                print("False")
                exit()

    print(True)