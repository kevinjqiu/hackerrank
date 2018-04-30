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

    def find_all_distances(self, s):
        q = deque([])
        unvisited = set([i for i in range(self.n)])
        dist = [-1 for _ in range(self.n)]

        dist[s] = 0
        q.append(s)
        unvisited.remove(s)

        while len(q) > 0:
            u = q.popleft()

            for v in self.adjacency_list.get(u, []):
                if v in unvisited:
                    dist[v] = dist[u] + 6
                    unvisited.remove(v)
                    q.append(v)

        print(' ' .join([str(dist_u) for i, dist_u in enumerate(dist) if i != s]))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
