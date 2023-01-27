def solution(arr):
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(arr[i])
        elif(arr[i] != arr[i-1]):
            result.append(arr[i])
    return result
        
arr = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]
arr3 = [0,0,0,1,0,0,3,4,4,4]
print(solution(arr))
print(solution(arr2))
print(solution(arr3))