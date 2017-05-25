# Build graph from pairs of word with its weight
# Produce function to get all paths from one node to other node
# minhvvu 2017-05-25

import networkx as nx

import graph_utils as gutil

def create_from_pairs(pairs):
    """
    Build graph from `pairs` of words.
    Accumulate weight for the edges that appear multiple time
    """
    DG = nx.DiGraph()
    for (n1, n2, w) in pairs:
        if DG.has_edge(n1, n2):
            DG.edge[n1][n2]['weight'] = w
        else:
            DG.add_edge(n1, n2, {'weight':w})
    return DG


def inverse_weights(G):
    """
    Make the larger weight become smaller by taking its inverse
    """
    for (n1, n2, w) in G.edges(data=True):
        G.edge[n1][n2]['weight'] = 1.0 / w['weight']


def build(pairs, outname):
    """
    Build graph from `pairs` of word
    and save the edges to text file `outname`
    """
    G = create_from_pairs(pairs)
    #inverse_weights(G)
    gutil.write_edges(G, outname)


def weighted_shortes_path(G, n1, n2):
    """
    Find the shortest path with weighted edges, using Dijkstra
    """
    return nx.dijkstra_path(G, n1, n2)


def sum_path(G, path):
    """
    Calculate sum of weight in each edges of `path`
    """
    sum_weight = 0
    for i in range(len(path)-1):
        n1, n2 = path[i], path[i+1]
        sum_weight += G[n1][n2]['weight']
    return sum_weight


def all_paths(G, src, dest, cutoff=4):
    """
    Find all paths from `src` to `dest` with default max depth in `cutoff`.
    The result paths are sorted by their weight sum, larger comes first.
    """
    return sorted([path
        for path in nx.all_simple_paths(G, src, dest, cutoff)],
         key=lambda path: -1 * sum_path(G, path))


def main():
    pairs = [("Hello", "there", 1.0),
            ("Hello", "there", 0.15),
            ("Hello", "world", 1.0),
            ("Nice", "to", 1.0),
            ("Nice", "to", 9.0),
            ("Nice", "meet", 0.5),
            ("Nice", "see", 0.4),
            ("to", "see", 1.0),
            ("to", "meet", 1.0),
            ("to", "you", 0.5),
            ("meet", "you", 1.0),
            ("meet", "him", 0.75),
            ("see", "you", 0.9),]

    outname = 'g_test'
    build(pairs, outname)
    G = gutil.read_edges(outname)
    gutil.print_graph(G)
    path = weighted_shortes_path(G, 'Nice', 'you')
    print(path)

    print(all_paths(G, 'Nice', 'you', cutoff=3))

if __name__ == '__main__':
    main()
