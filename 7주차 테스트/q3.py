def solution(strings, n):
    print(strings)
    answer = strings.sort(key = lambda x : x[n])
    return answer

print(solution(["sun","bed","car"], 1))