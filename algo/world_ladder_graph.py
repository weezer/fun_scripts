class Vertex:
    def __init__(self, k):
        self.id = k
        self.connectedTo = {}
        self.step = 0

    def add_neighbor(self, k, w):
        self.connectedTo[k] = w

    def __str__(self):
        return str(self.id) + ' Connected To: ' + str([str(x.id) + " weight: " + str(self.connectedTo[x]) for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, k):
        return self.connectedTo[k]


class Graph:
    def __init__(self):
        self.verticesList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        vx = Vertex(key)
        self.verticesList[key] = vx
        self.numVertices += 1
        return vx

    def get_vertex(self, k):
        if self.verticesList.get(k):
            return self.verticesList[k]
        else:
            return None

    def __contains__(self, item):
        return item in self.verticesList

    def add_edge(self, f, t, weight=0):
        if not self.get_vertex(f):
            self.add_vertex(f)
        if not self.get_vertex(t):
            self.add_vertex(t)
        self.get_vertex(f).add_neighbor(self.get_vertex(t), weight)

    def get_vertices(self):
        return self.verticesList.keys()

    def __iter__(self):
        return iter(self.verticesList.values())


def build_bucket(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                key_word = word[:i] + "_" + word[i+1:]
                if d.get(key_word):
                    d[key_word].append(word)
                else:
                    d[key_word] = [word]
    g = Graph()
    for i in d.values():
        for word1 in i:
            for word2 in i:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g

def bfs(graph, start, end):
    start_vertex = graph.get_vertex(start)
    import Queue
    q = Queue.deque()
    q.append(start_vertex)
    while len(q) > 0:
        check_vertex = q.popleft()
        print check_vertex.get_id()
        for i in check_vertex.get_connections():
            if i.step != 0:
                continue
            if i.get_id() == end:
                return check_vertex.step + 1
            i.step = check_vertex.step + 1
            q.append(i)
    return "not found"


if  __name__ == "__main__":
    g = build_bucket("4letter.txt")
    print bfs(g, "eggy", "doge")
