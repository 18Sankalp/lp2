def find(parent, i):
    if parent[i] == i: return i
    return find(parent, parent[i])
def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]: parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
        else: parent[yroot], rank[xroot] = xroot, rank[xroot]+1
def kruskal(nodes, edges):
    result, i, e = [], 0, 0 
    edges = sorted(edges, key=lambda item: item[2]) 
    parent, rank = list(range(max(max(edge[0], edge[1]) for edge in edges) + 1)), [0] * (max(max(edge[0], edge[1]) for edge in edges) + 1)
    while e < nodes - 1:
        u, v, w = edges[i]; i += 1; x, y = find(parent, u), find(parent, v)
        if x != y: e, result = e + 1, result + [(u, v, w)]; union(parent, rank, x, y)
    return result

nodes = int(input("Enter the number of nodes: "))
edges = [list(map(int, input().split())) for _ in range(int(input("Enter the number of edges: ")))]
result_kruskal = kruskal(nodes, edges)
print("\n".join(["Minimum Spanning Tree (Kruskal's Algorithm):"] + ["Edge: {} - {}, Weight: {}".format(*edge) for edge in result_kruskal]))
