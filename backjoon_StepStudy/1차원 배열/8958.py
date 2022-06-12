# 내 코드
n = int(input())
count = 0
sum = 0
for i in range(n):
    b = input()
    s = list(b)
    for j in range(len(s)):

        if(s[j] == 'O'):
            count += 1
            sum += count
        else:
            count = 0
    print(sum)
    count = 0
    sum = 0

# 모범 코드
# n = int(input())
# for i in range(n):
#     a = input()
#     b = list(a)
#     sum = 0
#     count = 1
#     for i in b:
#         if i == 'O':
#             sum += count
#             count += 1
#         else:
#             count = 1
#     print(sum)
