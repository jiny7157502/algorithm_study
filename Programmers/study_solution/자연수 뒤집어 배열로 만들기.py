def solution(n):
    n = list(map(int, str(n)))
    answer = []
    for i in range(len(n)):
        answer.append(n[len(n)-1-i])
    return answer

print(solution(12345))
print(solution(50000))