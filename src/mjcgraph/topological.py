#!/usr/local/bin/python3

import sys
from mjcgraph import symbolgraph
from mjcgraph import ddfo


class Topological():
    def __init__(self, Digraph):
        self.G = Digraph
        self.rank = [-1 for i in range(self.G.V)]
        # add cycle check later
        dfo = ddfo.DepthFirstOrder(self.G)
        self.order = dfo.get_reverse_post()

        for i, v in enumerate(self.order):
            self.rank[v] = i

    def get_order(self):
        return self.order

if __name__ == '__main__':

    SG = symbolgraph.SymbolGraph('../../data/jobs.txt', '/')
    print(SG.G)
    TS = Topological(SG.G)
    print(TS.G.G)
    names = SG.node_names()
    for v in TS.get_order():
        print(f'{v} {names[v]}')
