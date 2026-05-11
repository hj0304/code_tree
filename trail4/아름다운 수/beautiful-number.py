def backtrack(length):
    global cnt

    if length == N:
        cnt += 1
        return
    
    if length > N:
        return


    for i in range(1, 5):
        backtrack(length + i)

N = int(input())    # 몇자릿수

cnt = 0

backtrack(0)
print(cnt)