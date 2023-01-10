#!/usr/local/bin/python3

import sys

from mjcgraph import graph

class SymbolGraph():
    def __init__(self, infile, sc=' '):
        self.keys = [] # vertice index to name
        self.ST = {} # vertice name to index

        lines = open(infile).read().splitlines()
        for line in lines:
            res = line.split(sc)
            assert len(res) >= 2
            for i in res:
                if not i in self.ST:
                    self.ST[i] = len(self.ST)
                    self.keys.append(i)

        self.G = graph.Graph(len(self.ST))
        print(self.ST)

        lines = open(infile).read().splitlines()
        for line in lines:
            print()
            res = line.split(sc)
            print(f'len(res): {len(res)} - {res}')
            assert len(res) >= 2

            v = self.ST[res[0]]
            for i in res[1:]:
                w = self.ST[i]
                print(f'{i}: add edge from {v} ({res[v]}) -> {w} ({res[w]})')
                self.G.add_edge(v, w)


    def graph(self):
        return self.G


    def node_names(self):
        return self.keys

if __name__ == '__main__':
    sg = SymbolGraph('../../data/routes.txt')
    assert sg.G.V == 10
    assert sg.G.E == 18
    assert sg.keys[0] == 'JFK'
