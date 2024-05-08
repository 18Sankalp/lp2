def find(parent, i):
    if parent[i] == i: 
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot, yroot = find(parent, x), find(parent, y)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]: parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
        else: parent[yroot], rank[xroot] = xroot, rank[xroot]+1

def prims(nodes, edges, start):
    import heapq
    graph = [[] for _ in range(nodes + 1)]
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))  
    mst = []
    visited = [False] * (nodes + 1)
    min_heap = [(0, start, start
    while min_heap:
        cost, u, frm = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if u != frm:
            mst.append((frm, u, cost))
        for cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (cost, v, u))
    return mst

nodes = int(input("Enter the number of nodes: "))
edges = [list(map(int, input().split())) for _ in range(int(input("Enter the number of edges: ")))]
start_node = int(input("Enter the starting node for Prim's algorithm: "))
result_prim = prims(nodes, edges, start_node)

print("Minimum Spanning Tree (Prim's Algorithm):")
total_weight = 0
for edge in result_prim:
    print("Edge: {} - {}, Weight: {}".format(edge[0], edge[1], edge[2]))
    total_weight += edge[2]
print("Total Weight of MST:", total_weight)
