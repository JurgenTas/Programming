__author__ = 'J Tas'

from bag import Bag


class _Edge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight

    def either(self):
        return self._v

    def other(self, vertex):
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise ValueError('Wrong input')

    def compare_to(self, that):
        if self.weight() < that.weight():
            return -1
        elif self.weight() > that.weight():
            return 1
        else:
            return 0


class _DirectedEdge:
    def __init__(self, v, w, weight):
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight

    def from_vertex(self):
        return self._v

    def to_vertex(self):
        return self._w


class EdgeWeightedGraph:
    def __init__(self, n):
        self._v = n
        self._e = 0
        self._adj = [Bag() for i in range(self._v)]

    def num_vertex(self):
        return self._v

    def num_edges(self):
        return self._e

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self._adj[v].add(edge)
        self._adj[w].add(edge)
        self._e += 1

    def adjacent(self, v):
        return self.adj[v]

    def degree(self, v):
        return self.adj[v].size()

    def edges(self):
        l = Bag()
        for v in range(self._v):
            self_loops = 0
            for edge in self.adjacent(v):
                if edge.other(v) > v:
                    l.add(edge)
                elif edge.other(v) == v:
                    if self_loops % 2 == 0:
                        l.add(edge)
                    self_loops += 1
        return l


class EdgeWeightedDiGraph(EdgeWeightedGraph):
    def __init__(self, n):
        EdgeWeightedGraph.__init__(self, n)

    def add_edge(self, edge):
        v = edge.from_vertex()
        self._adj[v].add(edge)
        self._e += 1

    def edges(self):
        l = Bag()
        for v in range(self._v):
            for edge in self.adjacent(v):
                l.add(edge)
        return l


if __name__ == "__main__":
    e = _Edge(1, 0, 1)
    d = _Edge(1, 0, 2)
    print(e.compare_to(d))
