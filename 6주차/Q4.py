import math

A, B, V = map(int, input().split())
k = math.ceil((V-A)/(A-B)) + 1
print(int(k))