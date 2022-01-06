import sys

N = int(sys.stdin.readline())

array = list()

for i in range(N):
    num = int(sys.stdin.readline())
    array.append(num)

array = sorted(array)

for number in array:
    print(number)