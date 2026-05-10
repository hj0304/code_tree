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
        

n, m, k = map(int, input().split())

parent = list(range(n+1))
rank = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    union(a, b)
    
k_list = list(map(int,input().split()))

possible = True

for i in range(k-1):
    if find(k_list[i]) != find(k_list[i+1]):
        possible = False
        break

print(1 if possible else 0)