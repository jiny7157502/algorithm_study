import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    array.append([x, y])

array.sort(key=lambda x:x[0])

array.sort(key=lambda x:(x[1], x[0]))

for i in range(len(array)):
    print(array[i][0], array[i][1])