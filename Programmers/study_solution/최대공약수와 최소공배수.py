def solution(n, m):
    if m < n:
        n, m = m, n

    i, count = 2, 1
    while i < m:
        if n % i == 0 and m % i == 0:
            n = n // i
            m = m // i
            count *= i
            i = 2
        else:
            i += 1
        
    return [count, count*m*n]

print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]
print(solution(1, 5)) # [1, 5]
print(solution(64, 68)) # [4, 1088]
print(solution(99, 120)) # [3, 3960]

# 2 [64, 68]
# 2  32  34
#    16  17


#  3  [99, 120]
#      33   40
# =>  [3, 3960]