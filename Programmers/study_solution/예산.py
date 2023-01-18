def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    print(d)
    return len(d)

print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10))  # 4

# arr = [1,2,3,4,5]
# # print(sum(arr[0:2]))