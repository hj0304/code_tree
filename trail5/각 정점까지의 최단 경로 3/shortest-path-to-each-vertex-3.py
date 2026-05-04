import heapq

def dijkstra(start):
    queue = []
    dist[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist_start_to_curr, now = heapq.heappop(queue)

        if dist_start_to_curr > dist[now]:
            continue

        for neighbor, weight in graph[now]:
            cost = dist_start_to_curr + weight

            if dist[neighbor] > cost:
                dist[neighbor] = cost
                heapq.heappush(queue, (dist[neighbor], neighbor))


INF = float('inf')

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)


for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))


dijkstra(1)

for i in range(2, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])