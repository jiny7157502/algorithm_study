import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    array.append(i+1)

for i in range(N):
    if len(array) != 1:
        array.pop(0)
        array.append(array[0])
        array.pop(0)
    else:
        break

print(array[0])
