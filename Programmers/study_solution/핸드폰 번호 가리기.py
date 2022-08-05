def solution(phone_number):
    list_num = list(phone_number)
    
    for i in range(len(list_num)):
        if i < len(list_num) - 4:
            list_num[i] = "*"
            
    return "".join(list_num)

print(solution("01033334444"))
print(solution("027778888"))