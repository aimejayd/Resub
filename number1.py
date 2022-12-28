# First, let's go over the steps for Kruskal's algorithm:

# Sort the edges of the graph in non-decreasing order of their weights.
# Initialize a list of edges that will make up the minimum spanning tree (MST).
# For each edge in the sorted list of edges:
# If adding the edge to the MST would not create a cycle, add it to the MST.
# Return the MST.
# To implement this in a program, we can start by representing the graph as a list of tuples, where
# each tuple represents an edge and contains the vertices it connects and its weight. For example, 
# the graph in the question can be represented as:

graph = [    ('A', 'B', 3),    ('A', 'C', 1),    ('B', 'C', 3),    ('B', 'D', 1),    ('C', 'D', 1),    ('C', 'E', 5),    ('D', 'E', 4),]

def kruskal(graph):
    # Sort the edges by weight
    graph = sorted(graph, key=lambda x: x[2])

    # Initialize the MST as an empty list
    mst = []

    # Initialize the disjoint-set data structure with each vertex being in its own set
    sets = {vertex: {vertex} for vertex in set(vertex for edge in graph for vertex in edge[:2])}

    # Iterate over the sorted edges
    for u, v, weight in graph:
        # If adding the edge would not create a cycle, add it to the MST
        if sets[u] != sets[v]:
            mst.append((u, v, weight))
            sets[u] = sets[u] | sets[v]
            sets[v] = sets[u]

    return mst

# To draw the graph from the resulting MST, we can use a library such as NetworkX in Python. 

import networkx as nx

# Create a Graph object
G = nx.Graph()

# Add the edges from the MST to the Graph object
for u, v, weight in mst:
    G.add_edge(u, v, weight=weight)

# Draw the graph
nx.draw(G)

# For Prim's algorithm, the steps are similar:

# Initialize the MST with a single vertex and add it to a set of visited vertices.
# While the set of visited vertices is not equal to the set of all vertices:
# Find the minimum weight edge connecting a vertex in the set of visited vertices to a vertex not in the set.
# Add the vertex on the other end of the edge to the set of visited vertices and add the edge to the MST.
# Return the MST.
# We can implement Prim's algorithm as follows:

def prim(graph):
    # Initialize the MST with a single vertex
    mst = []
    visited = set()
min_
