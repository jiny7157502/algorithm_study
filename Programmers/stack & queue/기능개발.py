def solution(prog, spd):
    arr = []
    for i in range(len(prog)):
        if ((100 - prog[i]) % spd[i] == 0):
            x = (100 - prog[i]) // spd[i]
        else:
            x = (100 - prog[i]) // spd[i] + 1
        
        arr.append(x)

    print(arr)

    result = []
    sum = 0
    for i in range(len(arr)):
        sum += 1
        if(i == len(arr)-1):
            result.append(sum)
        elif(arr[i] < arr[i+1]):
            result.append(sum)
            sum = 0
    return result

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))
print(solution([10,20,30,40,50], [10,20,30,40,50])) # [2, 2, 3, 3, 5]