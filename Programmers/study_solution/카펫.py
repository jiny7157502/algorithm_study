def solution(brown, yellow):
    y = 0
    i = 1
    while True:
        if ((brown-4) // 2 - i) * i == yellow:
            y = i
            break
        else:
            i += 1
    return [yellow // y + 2, y + 2]
        
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))