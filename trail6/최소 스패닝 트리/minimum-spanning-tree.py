def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA != rootB:
        parent[rootB] = rootA
        return True
    
    return False

N, M = map(int, input().split())

parent = list(range(N+1))
graph = []

for i in range(M):
    a, b, weight = map(int, input().split())
    graph.append((weight, a, b))
    
graph.sort()
ans = 0

for i in graph:
    cost, a, b = i
    if union(a, b):
       ans += cost
       
print(ans)