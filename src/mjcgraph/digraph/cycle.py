#!/usr/bin/env python3

from mjcgraph.digraph import digraph
from collections import deque

class DirectedCycle():

    def __init__(self, DG):
        assert isinstance(DG, digraph.Digraph)
        self.marked = [False for i in range(DG.V)]
        self.onstack = [False for i in range(DG.V)]
        self.edgeto = [-1 for i in range(DG.V)]
        self.cycle = deque()

        for v in range(DG.V):
            if not self.marked[v]:
                self.dfs(DG, v)


    def dfs(self, DG, v):
        self.onstack[v] = True
        self.marked[v] = True
        for w in DG.adj(v):
            if self.has_cycle():
                return
            elif not self.marked[w]:
                self.edgeto[w] = v
                self.dfs(DG, w)
            elif self.onstack[w]:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeto[x]
                self.cycle.append(w)
                self.cycle.append(v)
        self.onstack[v] = False


    def has_cycle(self):
        return len(self.cycle) != 0


    def get_cycle(self):
        return self.cycle


if __name__ == '__main__':
    G = digraph.Digraph(4)
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    cycle = DirectedCycle(G)
    assert cycle.has_cycle() == False
    G.add_edge(3, 1)
    cycle = DirectedCycle(G)
    assert cycle.has_cycle() == True

    c = []
    while cycle.cycle:
        c.append(cycle.cycle.pop())

    print(f'cycle: {c}')
