from nltk.corpus import PlaintextCorpusReader
import networkx as nx

from collections import Counter
from itertools import chain
from itertools import tee

import graph_utils as gutil


def pairwise(itr):
    a, b = tee(itr)  # two version of itr
    next(b, None)    # b goes ahead one step
    return zip(a, b) # return iterator


def doc_to_sentences(root, ext):
    return PlaintextCorpusReader(root, ext).sents()


def doc_to_pairs(root, ext):
    return chain.from_iterable([pairwise(s)
        for s in doc_to_sentences(root, ext)])


def pairs_to_graph(pairs):
    G = nx.DiGraph()
    G.add_weighted_edges_from([(n1, n2, count)
        for ((n1, n2), count) in Counter(pairs).items()])
    return G


def sum_path(G, p):
    return sum([G[n1][n2]['weight'] for (n1, n2) in pairwise(p)])


def all_path(G, src, dest, cutoff=4):
    return sorted([path
        for path in nx.all_simple_paths(G, src, dest, cutoff)],
         key=lambda path: -1 * sum_path(G, path))


def train_graph(model_name, data_root, file_ext=r'.*\.txt'):
    pairs = doc_to_pairs(data_root, file_ext)
    G = pairs_to_graph(pairs)
    gutil.write_edges(G, model_name)


def example():
    pairs = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'b'), ('c', 'd')]

    G = pairs_to_graph(pairs)
    gutil.print_graph(G)
    gutil.draw_graph(G, 'example.png')
    gutil.write_edges(G, 'example.edge')

    res = all_path(G, 'a', 'd')
    print(res)


if __name__ == '__main__':
    data_root = '/home/minhvu/Data/dummy/'
    model_name = 'dummy_v1.edge'
    train_graph(model_name, data_root)
