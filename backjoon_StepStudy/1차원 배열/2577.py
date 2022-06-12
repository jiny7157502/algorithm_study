# result = 1
# count = 0
# for i in range(3):
#     a = int(input())
#     result = result * a
# result = str(result)
# for i in range(10):
#     for j in range(len(result)):
#         if(i == int(result[j])):
#             count += 1
#     print(count)
#     count = 0

result = 1
for i in range(3):
    a = int(input())
    result = result * a
result = str(result)
for i in range(10):
    print(result.count(str(i)))
