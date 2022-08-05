def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        sum_arr = []
        for j in range(len(arr1[0])):
            sum_arr.append(arr1[i][j] + arr2[i][j])
        answer.append(sum_arr)

    return answer


print(solution([[1],[2]], [[3],[4]])) # [[4], [6]]
# print(solution([[1,2],[2,3]], [[3,4],[5,6]])) # [[4,6], [7,9]]
# print(solution([[1,2,3],[2,3,4]], [[3,4,5],[5,6,7]])) # [[4,6,8], [7,9,11]]
# print(solution([[1,2],[2,3],[3,4]], [[3,4],[5,6],[7,8]])) # [[4,6], [7,9], [10,12]]
