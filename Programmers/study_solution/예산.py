def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)-1, 0, -1):
        if sum(d[0:i]) <= budget:
            answer = i+1
            break
    return answer

print(solution([1,3,2,5,4], 9)) # 3
# print(solution([2,2,3,3], 10))  # 4

# arr = [1,2,3,4,5]
# # print(sum(arr[0:2]))