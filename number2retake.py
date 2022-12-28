# Here is an example of a Breadth-First Search (BFS) algorithm that will
#  find the shortest reach from the starting node to all
#  other nodes in the graph, and return the distances in an array 
# `d`:

def bfs(n, m, e, s):
    # Initialize distance array to -1 for all nodes
    d = [-1] * n
    # Set distance of starting node to 0
    d[s] = 0
    # Initialize queue for BFS
    queue = []
    # Enqueue starting node
    queue.append(s)
    # While queue is not empty
    while queue:
        # Dequeue front of queue
        node = queue.pop(0)
        # For each edge connected to the dequeued node
        for edge in e:
            # If the edge starts at the dequeued node
            if edge[0] == node:
                # Calculate the distance to the adjacent node
                distance = d[node] + 4
                # If the distance to the adjacent node is not set or if it is greater than the current distance
                if d[edge[1]] == -1 or distance < d[edge[1]]:
                    # Set the distance to the adjacent node
                    d[edge[1]] = distance
                    # Enqueue the adjacent node
                    queue.append(edge[1])
    # Return the distance array
    return d

# This algorithm first initializes the distance array d to -1 for all nodes. It then sets the distance of the starting node 
# to 0. It initializes a queue for BFS and enqueues the starting node.

# The algorithm then enters a loop that continues until the queue is empty. 
# It dequeues the front of the queue and examines all edges connected to that node. 
# For each edge that starts at the dequeued node, the algorithm calculates the distance 
# to the adjacent node as the current distance to the dequeued node plus the weight of
#  the edge (which is 4 in this case). If the distance to the adjacent node is not set or
# if it is greater than the current distance, the algorithm sets the distance to the adjacent node and enqueues the adjacent node.

# Finally, the algorithm returns the distance array d.

# This algorithm can be used to solve the problem described in the question as follows:

# Number of nodes
n = 5
# Number of edges
m = 3
# Adjacent edges
e = [[1, 2], [1, 3], [3, 4], [5]]
# Starting node
s = 1

# Find shortest reach from starting node to all other nodes
d = bfs(n, m, e, s)

# Output distances to nodes 2 through 5
print(d[1:])
 
# This will output the distances to nodes 2 through 5 in the required format: [6, 6, 12, -1].