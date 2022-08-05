def solution(x):
    answer = True
    lx = map(int, str(x))
    if x % sum(lx) != 0:
        answer = False
    return answer

print(solution(12))