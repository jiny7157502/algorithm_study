def solution(num):
    count = 0
    while True:
        if count > 500:
            count = -1
            break
        elif num == 1:
            break
        else:
            if num % 2 == 0:
                num = num // 2
                count += 1
            elif num % 2 != 0:
                num = num * 3 + 1
                count += 1
    return count

print(solution(6)) # 8
print(solution(16)) # 4
print(solution(626331)) # -1