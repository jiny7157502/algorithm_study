import sys

n = int(sys.stdin.readline())
sum = []
for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    sum.append(A+B)
for i in range(n):
    print(sum[i])
