def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot
        else: 
            parent[yroot], rank[xroot] = xroot, rank[xroot]+1

def kruskal(nodes, edges):
    result, i, e = [], 0, 0 
    edges = sorted(edges, key=lambda item: item[2]) 
    parent, rank = list(range(max(max(edge[0], edge[1]) for edge in edges) + 1)), [0] * (max(max(edge[0], edge[1]) for edge in edges) + 1)
    while e < nodes - 1:
        u, v, w = edges[i]; i += 1; x, y = find(parent, u), find(parent, v)
        if x != y: e, result = e + 1, result + [(u, v, w)]; union(parent, rank, x, y)
    return result

def prim(nodes, edges):
    max_node = max(max(edge[0], edge[1]) for edge in edges) + 1  
    adj, visited, result, edge_list = {i: [] for i in range(1, max_node)}, [False] * max_node, [], [(0, 0, 1)]
    for u, v, w in edges: adj[u].append((v, w)); adj[v].append((u, w))
    while edge_list:
        w, u, v = min(edge_list, key=lambda item: item[0]); edge_list.remove((w, u, v))
        if not visited[v]: visited[v], result = True, result + [(u, v, w)]
        for next_node, weight in adj[v]:
            if not visited[next_node]: edge_list.append((weight, v, next_node))
    return result[1:] 

def dijkstra(nodes, edges, start, end):
    max_node = max(max(edge[0], edge[1]) for edge in edges) + 1
    adj, dist, visited = {i: [] for i in range(1, max_node)}, [float('inf')] * max_node, [False] * max_node 
    dist[start] = 0
    for u, v, w in edges: adj[u].append((v, w)); adj[v].append((u, w))
    for _ in range(max_node):
        u = min((i for i in range(1, max_node) if not visited[i]), key=lambda x: dist[x], default=-1)
        if u == -1: break
        visited[u] = True
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]: dist[v] = dist[u] + weight
    path, total_weight = [], 0
    u = end
    while u != start:
        for v, w in adj[u]:
            if dist[u] == dist[v] + w:
                path.append(u)
                total_weight += w
                u = v
                break
    path.append(start)
    path.reverse()
    return path, total_weight

nodes = int(input("Enter the number of nodes: "))
edges = []
print("Enter edges in the format 'node1 node2 weight': ")
for _ in range(int(input("Enter the number of edges: "))):
    edges.append(tuple(map(int, input().split())))
result_kruskal = kruskal(nodes, edges)
result_prim = prim(nodes, edges)
start_node = int(input("Enter the starting node for prim's and Dijkstra's algorithm: "))
end_node = nodes
result_dijkstra, total_weight = dijkstra(nodes, edges, start_node, end_node)

print("Minimum Spanning Tree (Kruskal's Algorithm):", *["Edge: {} - {}, Weight: {}".format(*edge) for edge in result_kruskal], sep="\n")
print("\nMinimum Spanning Tree (Prim's Algorithm):", *["Edge: {} - {}, Weight: {}".format(*edge) for edge in result_prim], sep="\n")
print("\nShortest Path from node {} to node {} (Dijkstra's Algorithm):".format(start_node, end_node))
print("Path:", result_dijkstra, "Total Weight:", total_weight)
