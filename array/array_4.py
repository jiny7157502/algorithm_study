import sys

N = int(sys.stdin.readline())

array = []
real_array = []

for _ in range(N):
    word = sys.stdin.readline()
    word = word.rstrip()
    array.append(word)

# set 함수로 중복 제거 후 리스트 형으로 변환
array = list(set(array))

# 알파벳 순서대로 정렬
array.sort()

# 길이 순서대로 정렬
array.sort(key=len)

print(array)