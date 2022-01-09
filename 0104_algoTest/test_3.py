# import sys

# a, b = map(int, sys.stdin.readline().split())

# for i in range(a):

# 입력
inputData = input("입력 : ").split()

# 숫자를 넣기위한 변수
numbers = list()

# 최대값 / null
maxNumber = None

for data in inputData:
    # 7 3 4 -> 4 3 7 정렬을 역으로 한다.
    number = int(data[::-1])
    # numbers라는 배열에 대입
    numbers.append(number)

    # None이거나 혹은 기존의 최대값보다 현재값이 클 경우
    if maxNumber == None or number > maxNumber:
        maxNumber = number

print(maxNumber)