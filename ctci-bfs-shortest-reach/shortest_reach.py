from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.n = n  # number of nodes
        # self.nodes = list(range(n))
        self.adjacency_list = defaultdict(list)

    def connect(self, u, v):
        """Connect node u with node v
        """
        self.adjacency_list[u].append(v)

    def bfs(self, start, end):
        num_edges = 0
        visited = set([])
        to_visit = deque([])

        to_visit.append(start)
        while len(to_visit) > 0:
            v = to_visit.popleft()
            connected = self.adjacency_list.get(v, [])
            if end in connected:
                num_edges += 1
                return num_edges * 6
            num_edges += 1
            for node in connected:
                if node not in visited:
                    to_visit.append(node)
        return -1

    def find_all_distances(self, s):
        retval = []
        for i in range(self.n):
            if i == s:
                continue
            retval.append(self.bfs(s, i))
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
