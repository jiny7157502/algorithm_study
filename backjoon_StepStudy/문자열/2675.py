# n = int(input())
# for i in range(n):
#     a, b = input().split()
#     a = int(a)
#     result = []
#     for i in range(len(b)):
#         for j in range(a):
#             result.append(b[i])
#     result = "".join(result)
#     print(result)

n = int(input())
for i in range(n):
    num, str = input().split()
    result = ""
    for i in str:
        result += i * int(num)
    print(result)
