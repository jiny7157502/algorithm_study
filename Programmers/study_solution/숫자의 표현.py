def solution(n):
    answer = 0
    for i in range(1, n+1, 2):
        if n % i == 0:
            answer += 1
    return answer
    
# def solution(n):
#     answer = 0
#     for i in range(1, n+1 % 2):
#         temp = 0
#         for j in range(i, n+1 % 2):
#             temp += j
#             if temp == n:
#                 answer += 1
#                 break
#     return answer

print(solution(10)) # 4
