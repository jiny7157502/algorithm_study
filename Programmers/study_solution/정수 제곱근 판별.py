def solution(n):
    i, answer = 1, 1
    while i < n:
        i += 1
        if n // i == i and n % i == 0:
            break
    return (i+1)**2 if n == 1 or i != n else -1

# 런타임 에러
# def solution_ver2(n):
#     i = 1
#     while i < n:
#         if n == i**2:
#             break
#         i += 1
#     return (i+1)**2 if n == 1 or i != n else -1

print(solution(121)) # 144
print(solution(5)) # -1