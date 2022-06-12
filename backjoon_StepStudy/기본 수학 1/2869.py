A, B, V = map(int, input().split())
result = 0
count = 1
while result != V:
    result += A
    if result < V:
        result -= B
        count += 1
    else:
        break

print(count)
