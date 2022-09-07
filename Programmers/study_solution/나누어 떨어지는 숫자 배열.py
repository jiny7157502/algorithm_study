def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer) if len(answer) != 0 else [-1]

print(solution([5, 9 ,7 ,10], 5)) # [5, 10]
print(solution([2, 36, 1, 3], 1)) # [1, 2, 3, 36]
print(solution([3, 2, 6], 10)) # [-1]