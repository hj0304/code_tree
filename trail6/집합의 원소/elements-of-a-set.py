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


for i in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)