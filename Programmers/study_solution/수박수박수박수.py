def solution(n):
    s = "수박"
    if n % 2 == 0:
        return s*(n//2)
    else:
        return s*(n//2) + "수"

print(solution(3))
print(solution(4))