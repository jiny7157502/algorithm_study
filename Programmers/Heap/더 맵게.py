def solution(scoville, k):
    count = 0
    scoville.sort()
    while scoville[0] < k:
        if len(scoville) == 1:
            count = -1
            break
        else:
            new = scoville[0] + scoville[1] * 2
            scoville.append(new)
            scoville.remove(scoville[0])
            scoville.remove(scoville[0])
            scoville.sort()
            count += 1

    return count

print(solution([1,2,3,9,10,12], 7)) # 2
print(solution([1,1,1,1,1], 7))
print(solution([1,2,3,9,10,12], 7))