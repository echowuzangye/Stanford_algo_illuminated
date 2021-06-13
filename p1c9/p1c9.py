import heapq
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}
# for item in graph["A"]:
#     print(item)

# load course data

dijkstra_graph = {}
with open("dijkstraData.txt")as file:
    content = file.read()
    content = content.split('\n')
    content.pop()
    for i in range(len(content)):
        content[i] = content[i].split()
        dijkstra_graph[content[i][0]] = {k.split(",")[0]: int(k.split(",")[1]) for k in content[i][1:]}
    # print(dijkstra_graph)


def init_dist(g, s):
    """ distance initialization: 0 for start vertex; infinite for the rest vertex"""
    distance = {s: 0}
    for v in g:
        if v != s:
            distance[v] = math.inf
    return distance


# BFS implementation and shortest paths
def dijkstra(graph, s):
    pq = []
    heapq.heappush(pq, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_dist(graph, s)
    while len(pq) > 0:
        pair = heapq.heappop(pq)
        dist = pair[0]
        vert = pair[1]
        seen.add(vert)
        nodes = graph[vert]
        for w in nodes:
            if w not in seen:
                if dist + graph[vert][w] < distance[w]:
                    distance[w] = dist + graph[vert][w]
                    heapq.heappush(pq, (distance[w], w))
                    parent[w] = vert
    return parent, distance


p, d = dijkstra(dijkstra_graph, '1')
print(p)
print(d['7'],d['37'],d['59'],d['82'],d['99'],d['115'],d['133'],d['165'],d['188'],d['197'])
