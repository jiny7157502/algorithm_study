def solution(arr):
    answer = [[arr[0]]]
    for i in range(len(answer)):
        if arr[i] == arr[i-1]:
            answer.append(arr[i])
        return answer
    
print(solution([1,1,3,3,0,1,1])) # [1, 3, 0, 1]
print(solution([4,4,4,3,3])) #[4, 3]