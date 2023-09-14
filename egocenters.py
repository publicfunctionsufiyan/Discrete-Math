import networkx as nx

G = nx.Graph()
edgelist = nx.read_edgelist('facebook_combined.txt', nodetype=int, create_using=nx.Graph())
pseudocenters = [0, 107, 1684, 1912, 3437, 348, 612, 3980, 414, 686, 698]

edgelist = edgelist.edges


def find_impostor(edgelist, pseudocenters):
    G = nx.Graph()
    G.add_edges_from(edgelist)
    for y in pseudocenters:
        a = G.copy()
        a.remove_node(y)
        count = nx.number_connected_components(a)
        if count == 1:
            return y


find_impostor(edgelist, pseudocenters)