import networkx as nx
from itertools import chain

from helper import pairwise
import graph_utils as gutil


def score_path(G, p):
    return sum([G[n1][n2]['weight']
        for (n1, n2) in pairwise(p)]) / len(p)


def find_paths(G, src, dest, cutoff):
    return sorted(
        [path for path in nx.all_simple_paths(G, src, dest, cutoff)],
        key=lambda path: -1 * score_path(G, path))


def suggest(G, words, cutoff=4):
    multi_paths = [find_paths(G, w1, w2, cutoff)
            for (w1, w2) in pairwise(words)]
    return [chain(*path) for path in zip(*multi_paths)]


if __name__ == '__main__':
    model_name = 'dummy_v1.edge'
    G = gutil.read_edges(model_name)
    gutil.draw_graph(G, 'dummy_v1.png')
    key_words = ["machine", "algorithm"]
    res = suggest(G, key_words, cutoff=5)
    for r in res: print(list(r))

