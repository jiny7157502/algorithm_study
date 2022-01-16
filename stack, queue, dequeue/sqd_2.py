import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    num = int(sys.stdin.readline())

    if num != 0:
        array.append(num)
    else:
        array.pop()

print(sum(array))