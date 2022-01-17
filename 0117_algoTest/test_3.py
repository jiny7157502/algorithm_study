import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    num = int(sys.stdin.readline())
    array.append(num)

array_2 = []
print(array)

for i in range(N):
    for j in range(1, N):
        print(str(array[i]) + " " + str(array[j]))
        if i+j > len(array):
            break
        else:
            if array[i] < array[i+j]:
                if i+j > len(array):
                    print(-1)
                    break
                else:
                    print(array[i+j])
                    break