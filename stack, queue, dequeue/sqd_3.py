import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    num = int(sys.stdin.readline())
    array.append(num)

for i in range(N):
    for j in range(N):
        if i == 0:
            print("+")
            j = N - array[i] + 1
        print("-")
        if i == N-1:
            a
        elif i > 0 and i < N-1:
            if array[i-1] > array[i]:
                if array[i-1] - array[i] == 1:
                    print("-")
    