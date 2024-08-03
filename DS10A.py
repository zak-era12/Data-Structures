#Write a program to generate the adjacency matrix.
def generate_adjacency_matrix(nodes, edges):
    matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for edge in edges:
        matrix[edge[0]][edge[1]] = 1
        matrix[edge[1]][edge[0]] = 1
    return matrix

# Example Usage
nodes = 4
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
adj_matrix = generate_adjacency_matrix(nodes, edges)
for row in adj_matrix:
    print(row)
