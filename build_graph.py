# Build graph from pairs of word with its weight
# Using negative weight for applying shortest-part algo

import networkx as nx

import graph_utils as gutil

def create_from_pairs(pairs):
    DG = nx.DiGraph()
    for (n1, n2, w) in pairs:
        if DG.has_edge(n1, n2):
            DG.edge[n1][n2]['weight'] = w
        else:
            DG.add_edge(n1, n2, {'weight':w})
    return DG


def normalize_weights(G):
    for (n1, n2, w) in G.edges(data=True):
        G.edge[n1][n2]['weight'] = 1.0 / w['weight']


def build(pairs, outname):
    G = create_from_pairs(pairs)
    #normalize_weights(G)
    gutil.write_edges(G, outname)


def weighted_shortes_path(G, n1, n2):
    return nx.dijkstra_path(G, n1, n2)


def sum_path(G, path):
    sum_weight = 0
    for i in range(len(path)-1):
        n1, n2 = path[i], path[i+1]
        sum_weight += G[n1][n2]['weight']
    return sum_weight


def all_paths(G, src, dest):
    return sorted([path
        for path in nx.all_simple_paths(G, src, dest)],
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

    print(all_paths(G, 'Nice', 'you'))

    
if __name__ == '__main__':
    main()
