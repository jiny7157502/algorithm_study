import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split(" "))
    age = int(age)
    name = name.rstrip()
    array.append([age, name])

array.sort(key=lambda x:x[0])

for i in range(N):
    print(array[i][0], array[i][1])