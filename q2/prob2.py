# Justin Ventura

import sys
import math

class Graph:
    def __init__(self, V):
        self.vertices = V
        # map from v to all u neighbors


def is_vcover(G, S):
    edge_set = set()
    for v in G.vertices.keys():
        for j in G.vertices[v]:
            edge_set.add((v, j))


    for i in edge_set:
        is_cover = False
        for j in S:
            if j in i:
                is_cover = True

        if not is_cover:
            return False

    return True


def min_cover(G):
    options = []
    S = set()
    for i in range(0, int(math.pow(2, len(G.vertices)))):
        for j in range(0, len(G.vertices)):
            if (i & (1 << j)):
                S.add(j+1)

        if is_vcover(G, S) and (len(S) <= (len(G.vertices.keys()) - 1)):
            options.append(len(S))
        else:
            S.clear()

    return min(options)

if __name__ == '__main__':
    lines = sys.stdin.read().split('\n')
    R, I = lines[:2]
    verts = {}
    newl = lines[2:]
    for i in range(len(newl)-1):
        verts[i+1] = tuple(map(int, newl[i].split(' ')))

    G = Graph(verts)
    print(min_cover(G))
    print('Justin Ventura')
