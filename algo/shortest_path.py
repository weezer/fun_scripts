x = """3 2 0 2
1 2 3
0 1 10
1 2 11"""


def build_graph(lst):
    start = lst[0][2]
    end = lst[0][3]
    g = Graph()
    for i in range(lst[1]):
        g.add_vertex(i, lst[1][i])

    for i in range(2, len(lst)):
        g.add_edge(lst[i][0], lst[i][1], lst[i][2])
    result = {}
    find_shortest_path(g, start, end, 0, [], {})

class Vertex:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.neighbor = {}

    def add_neighbor(self, v, weight):
        self.neighbor[v] = weight

    def get_weight(self, d):
        return self.neighbor[d]

    def get_value(self):
        return self.value

    def get_id(self):
        return self.name

    def get_neighbor_weight(self, v):
        return self.neighbor[v]

    def get_neighbor_list(self):
        return self.neighbor.keys()

    def __str__(self):
        return str(self.name) + " connected to: " + str([x.name + " weight: " + y for x, y in self.neighbor])


class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex(self, name):
        return self.vertices.get(name)

    def add_vertex(self, name, weight):
        vx = Vertex(name, weight)
        self.vertices[name] = vx
        return vx

    def add_edge(self, j, k, weight):
        if not self.get_vertex(j):
            vj = self.add_vertex(j)
        if not self.get_vertex(k):
            vk = self.add_vertex(k)
        vj.add_neighbor(vk, weight)
        vk.add_neighbor(vj. weight)


def find_shortest_path(g, start_point, end_point, path, weight, result):
    if start_point == end_point:
        result[path] = weight
        return
    for i in start_point.get_neighbor_list():
        if i not in path:
            find_shortest_path(g, g.get_vertex(i), end_point, path + [i], weight + start_point.get_weight(i), result)
