def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x:x*3, reverse=True) # ASCII 값으로 치환하여 정렬
    return str(int(''.join(num)))

# 9 5 34 3 30
num = [3, 30, 34, 5, 9]
print(solution(num))