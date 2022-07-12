def solution(nums):
    answer = 0
    set_nums = list(set(nums))
    if int(len(nums) / 2) < len(set_nums):
        answer = int(len(nums) / 2)
    else:
        answer = len(set_nums)
    return answer

print(solution([3,1,2,3]))     # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2