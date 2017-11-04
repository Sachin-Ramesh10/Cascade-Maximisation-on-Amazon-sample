import networkx as nx

G = nx.DiGraph()
newG = {}
rand_no = 0.5
k = 10
S = []
V = []
Activated_Nodes = {}
edge_list = []

with open("Amazon0302.txt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        else:
            edge = line.split()
            edge_list.append(edge)
G.add_edges_from(edge_list)

#creates a dictionary of nodes and their weights based on their out degree
def create_weights():
    for k in G.edges():
        a, b = k
        p = 1 / G.out_degree(a)
        newG[a] = p
        if newG[a] > rand_no:
            V.append(a)

# creates the dictionary of nodes and thier corresponding Activated number of nodes
def get_activated_node_list():
    for l in V:
        Activated_Nodes[l] = get_nodes_activated_list(l, l)

# recursively calculates the total number of activated neighbors
def get_nodes_activated_list(n, m):
    AN = {}
    neighbors = G.neighbors(m)
    AN[n] = len(neighbors) + 1
    for ne in neighbors:
        if ne in V:
            neighbors1 = G.neighbors(ne)
            AN[n] = len(neighbors1) + int(AN.get(n))
            if n != ne:
                get_nodes_activated_list(n, ne)
    return int(AN.get(n))

# computes the total number of maximum cascading nodes
def get_S():
    i = 0
    while i != k:

        if not S:
            S.append(max(Activated_Nodes, key=Activated_Nodes.get))
            del Activated_Nodes[max(Activated_Nodes, key=Activated_Nodes.get)]
            i = i + 1
        else:
            S.append(max(Activated_Nodes, key=Activated_Nodes.get))
            del Activated_Nodes[max(Activated_Nodes, key=Activated_Nodes.get)]
            i = i + 1

    print("The Nodes constituting Maximum Cascading are\t" + str(S))


create_weights()
get_activated_node_list()
get_S()
