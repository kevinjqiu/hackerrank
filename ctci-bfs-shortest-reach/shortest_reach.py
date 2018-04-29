from collections import defaultdict, deque
from operator import itemgetter


MAX_INTEGER = 2 ** 32


class Graph:
    def __init__(self, n):
        self.n = n  # number of nodes
        self.adjacency_list = defaultdict(list)

    def connect(self, u, v):
        """Connect node u with node v
        """
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def shortest_path(self, start, end):
        q = set(list(range(self.n)))  # vertices to visit
        dist = [MAX_INTEGER] * self.n
        prev = [None] * self.n

        dist[start] = 0

        while len(q) > 0:
            dist_u, u = min([(dist[u], u) for u in q], key=itemgetter(0))
            q.remove(u)

            for v in self.adjacency_list.get(u, []):
                alt = dist_u + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return -1 if dist[end] == MAX_INTEGER else dist[end] * 6

    def find_all_distances(self, s):
        retval = []
        for i in range(self.n):
            if i == s:
                continue
            retval.append(self.shortest_path(s, i))
        print(' '.join(map(str, retval)))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
