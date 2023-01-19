def solution(arr):
    result = []
    status = "yes"
    for i in range(len(arr)-1):
        if(status == "yes"):
            result.append(arr[i])
            if(arr[i] == arr[i+1]):
                status = "no"
        else:
            if(arr[i] != arr[i+1]):
                status = "yes"
    print(result)
        
arr = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]
arr3 = [0,0,0,1,0,0,3,4,4,4]
solution(arr)
solution(arr2)
solution(arr3)