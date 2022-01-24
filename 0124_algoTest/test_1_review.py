import sys

n = int(input()) # 4

A = list(map(int, sys.stdin.readline().split())) # 3 5 2 7

answer = [-1]*n # answer 값 [-1, -1, -1, -1]로 저장

stack = []

stack.append(0)

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
