import heapq
def dijkstra(graph, start, end):
    d, q, prev = [float('inf')] * len(graph), [(0, start)], [None] * len(graph)
    d[start] = 0
    while q:
        dist, u = heapq.heappop(q)
        if dist > d[u]: continue
        if u == end: break
        for w, v in graph[u]:
            alt = dist + w
            if alt < d[v]: d[v], prev[v] = alt, u; heapq.heappush(q, (alt, v))
    path = []
    while end is not None: path.append(end); end = prev[end]
    path.reverse()
    return d[path[-1]], path

n, e = int(input("enter no.of Nodes: ")), [list(map(int, input().split())) for _ in range(int(input("Edges: ")))]
g = [[] for _ in range(n + 1)] 
for u, v, w in e: g[u].append((w, v)); g[v].append((w, u))
s, e = int(input("Start: ")), n

shortest_distance, shortest_path = dijkstra(g, s, e)
print("\nShortest Distance from node {} to node {} (Dijkstra's Algorithm):".format(s, e))
print("Shortest Distance:", shortest_distance)
print("Shortest Path:", shortest_path)
