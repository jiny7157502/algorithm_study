def solution(n):
    result = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        result += str(remainder)
    return int(result, 3)

print(solution(45))  # 7
print(solution(125)) # 229