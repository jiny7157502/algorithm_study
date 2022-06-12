result = []
b = 0
for i in range(10):
    a = int(input())
    a = a % 42
    result.append(a)
result2 = set(result)
print(len(result2))
