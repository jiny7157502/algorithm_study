import sys

num = int(sys.stdin.readline())

num = str(num)

array = []

for number in num:
    array.append(number)

array = sorted(array, reverse=True)

for i in range(len(array)):
    print(array[i], end="")