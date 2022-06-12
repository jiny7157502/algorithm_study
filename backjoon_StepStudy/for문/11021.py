n = int(input())
result = []
for i in range(n):
    A, B = map(int, input().split())
    result.append(A + B)
for i in range(n):
    print("Case #" + str(i+1) + ":", result[i])
