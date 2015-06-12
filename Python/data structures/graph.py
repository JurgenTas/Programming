__author__ = 'Jurgen Tas'

from bag import _Bag
 
class Graph():
 
    def __init__(self, n):
        self.v = n
        self.e = 0
        self.adj = [_Bag() for i in range(self.v)]
 
    def num_vertex(self):
        return self.v
 
    def num_edges(self):
        return self.e
 
    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.e += 1
 
    def adjacent(self, v):
        return self.adj[v]
 
    def degree(self, v):
        return self.adj[v].size()
 
 
class Digraph(Graph):
 
    def __init__(self, n):
        Graph.__init__(self, n)
 
    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.e += 1
 
    def reverse(self):
        reverse = Graph(self.v)
        for i in range(self.v):
            for j in self.adjacent(i):
                reverse.add_edge(j, i)
        return reverse
 
 
class DepthFirstSearch:
   
    def __init__(self, g, s):
        self._marked = [False] * g.num_vertex()
        self._count = 0
        self._dfs(g, s)
       
    def _dfs(self, g, v):
        self._count += 1
        self._marked[v] = True
        for w in g.adjacent(v):
            if not self._marked[w]:
                self._dfs(g, w)
 
    def is_marked(self, v):
        return self._marked[v]
   
    @property
    def count(self):
        return self._count
 
 
if __name__ == "__main__":
 
    g = Digraph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    dfs = DepthFirstSearch (g, 0)
    print(dfs.is_marked(3))