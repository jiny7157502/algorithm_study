import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    num = int(sys.stdin.readline())
    array.append(num)

for i in range(N):
    if i == 0:
        for _ in range(array[i]):
            print("+")
        print("-")
    else:
        if(array[i] > array[i+1])
