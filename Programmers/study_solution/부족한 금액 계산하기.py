def solution(price, money, count):
    result = 0
    for i in range(1, count+1):
        result += price*i
    return result - money if result >= money else 0

print(solution(3, 20, 4)) # 10