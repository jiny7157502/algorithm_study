def solution(arr):
    arr2 = list(map(str, arr))
    result = True
    sum = 0
    for i in range(len(arr2)):
        if(sum < 0):
            result = False
            break
        else:            
            if(arr2[i] == "("):
                sum += 1
            else:
                sum += -1

    if(sum != 0):
        result = False
    return result

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))