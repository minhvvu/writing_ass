# Utils for print, read, write graph
# Produce a simple version of draw function to visualize graph
# minhvvu 2017-05-25

import networkx as nx
import matplotlib.pyplot as plt
import sys


def write_edges(H, outname=None, delimiter=';'):
    """
    Write list of edges to file `outname`.
    If the file name is not passed, print to screen.
    """
    if outname and outname != "":
        nx.write_edgelist(H, path=outname, delimiter=delimiter)
    else:
        nx.write_edgelist(H, sys.stdout.buffer)


def read_edges(inname, delimiter=';'):
    """
    Create a new graph by reading list of edges from file.
    """
    return nx.read_edgelist(path=inname, delimiter=delimiter)


def write_adj(H, outname=None):
    """
    Write adjacency list of each vertex to file `outname`.
    If the file name is not passed, print to screen.

    """
    if outname and outname != "":
        nx.write_adjlist(H,path= outname)
    else:
        nx.write_adjlist(H, sys.stdout.buffer)


def print_graph(H):
    """
    Print all edges of weighted and non-weighted graph.
    """
    for edge in H.edges(data=True):
        if (len(edge) == 2):
            print(edge[0], ' -> ', edge[1])
        elif(len(edge) == 3):
            print(edge[0], ' => ', edge[1], edge[2])


def draw_graph(H, outname=None):
    """
    Draw directed graph with weights
    https://networkx.readthedocs.io/en/stable/examples/drawing/chess_masters.html
    """
    edgewidth=[]
    for (u,v,d) in H.edges(data=True):
        edgewidth.append(len(H.get_edge_data(u,v)))

    pos=nx.spring_layout(H,iterations=20)

    nx.draw_networkx_nodes(H,pos,node_color='w',alpha=0.4)
    nx.draw_networkx_edges(H,pos,alpha=0.4,node_size=0,width=edgewidth,edge_color='k')
    nx.draw_networkx_labels(H,pos,fontsize=14)

    plt.axis('off')
    #plt.figure(figsize=(8,8))
    if (outname and outname != ''):
        plt.savefig(outname)
    else:
        plt.show()

