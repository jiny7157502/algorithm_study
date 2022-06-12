def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)


n = int(input())
print(fibonacci(n))

# N = int(input())

# a = 0
# b = 1
# for i in range(N+1):
#     if i == 0:
#         if N == i:
#             print(a)
#     elif i == 1:
#         if N == i:
#             print(b)
#     else:
#         result = a + b
#         if N == i:
#             print(result)
#         a = b
#         b = result
