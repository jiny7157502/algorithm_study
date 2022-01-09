import sys

n = int(sys.stdin.readline())

# array = list()
array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array = sorted(array)
# array.sort()

for i in range(len(array)):
    print(array[i])

# 배열에 있는 것을 하나씩 출력하기 위함
# for number in array:
#   print(number)