M = int(input())
N = int(input())
sosu = []
for i in range(M, N+1):
    err = 0
    count = 0
    for j in range(2, i):
        if i % j == 0:
            err += 1
    if err == 0:
        sosu.append(i)

result = 0
for i in sosu:
    result += i
if result == 0:
    print(-1)
else:``
    print(result)
    print(sosu[0])
