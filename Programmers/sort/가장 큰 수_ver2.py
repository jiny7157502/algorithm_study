from functools import cmp_to_key

def compare(x, y):
    if x+y > y+x:
        return -1
    elif x+y == y+x:
        return 0
    else:
        return 1

def solution(num):
    num = list(map(str, num))
    num = sorted(num, key=cmp_to_key(compare))
    return str(int(''.join(num)))

num = [3, 30, 34, 5, 9]
print(solution(num))