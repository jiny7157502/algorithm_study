n = int(input())
a1 = []
b1 = []
result = []
for i in range(n):
    a, b = map(int, input().split())
    a1.append(a)
    b1.append(b)
    result.append(a+b)
for i in range(n):
    print("Case #" + str(i+1) + ":", a1[i], "+", b1[i], "=", result[i])
