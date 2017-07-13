class Vertex:
    def __init__(self, id):
        self.id = id
        self.connected = {}

    def add_neighbor(self, k, v=0):
        self.connected[k] = v

    def get_neighbor(self):
        return self.connected

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.get_id()) + " connected: " + str([x.get_id() for x in self.get_neighbor().keys()])


class Graph:
    def __init__(self):
        self.vertices_list = {}

    def get_vertex(self, id):
        return self.vertices_list.get(id)

    def add_vertex(self, id):
        if not self.get_vertex(id):
            self.vertices_list[id] = Vertex(id)

    def add_edge(self, id1, id2):
        if not self.get_vertex(id1):
            self.add_vertex(id1)
        if not self.get_vertex(id2):
            self.add_vertex(id2)
        self.get_vertex(id1).add_neighbor(Vertex(id2))
        self.get_vertex(id2).add_neighbor(Vertex(id1))

    def set_connect(self, id1, id2):
        if not self.get_vertex(id1):
            self.add_vertex(id1)
        if not self.get_vertex(id2):
            self.add_vertex(id2)
        self.get_vertex(id1).get_neighbor()[self.get_vertex(id2)] = 1
        self.get_vertex(id2).get_neighbor()[self.get_vertex(id1)] = 1

    def get_vertices(self):
        return self.vertices_list


def find_maximum_pair(lst):
    start_points = lst[0][0]
    pair_points = lst[0][1]
    g = Graph()
    for i in lst[1:]:
        if i[0] == -1 and i[1] == -1:
            break
        g.add_edge(i[0], i[1])
    pair_g = [-1 for x in range(start_points)]

    for k in g.get_vertices().values():
        print g.get_vertex(k.get_id())

    for i in range(1, start_points + 1):
        find_augment_path(g, pair_g, i)

    return pair_g


def check_valid_neighbor(g1, neighbor):
    for i in neighbor:
        if i.get_id() not in g1:
            return i.get_id()


def find_augment_path(g1, g2, point):
    vx = g1.get_vertex(point)
    # print str(type(vx)) + str(vx)
    # print g2
    vn = vx.get_neighbor()
    valid_neighbor = check_valid_neighbor(g2, vn.keys())
    if valid_neighbor:
        g2[point - 1] = valid_neighbor
        return True
    for i in vn.keys():
        print str(i) + " outside " + str(point)
        if g2.index(i.get_id()) + 1 != point and find_augment_path(g1, g2, g2.index(i.get_id()) + 1):
            g2[point - 1] = i.get_id()
            return True
    return False


if __name__ == "__main__":
    lst = [[3, 6], [1,4], [1,5], [2,5], [2,6], [3,4]]
    pair = find_maximum_pair(lst)
    for i in pair:
        print i