num1, num2 = input().split()
# real_num1 = int(num1[2] + num1[1] + num1[0])
# real_num2 = int(num2[2] + num2[1] + num2[0])
real_num1 = int(num1[::-1])
real_num2 = int(num1[::-1])

# if real_num1 > real_num2:
#     print(real_num1)
# else:
#     print(real_num2)
print(real_num1) if real_num1 > real_num2 else print(real_num2)
