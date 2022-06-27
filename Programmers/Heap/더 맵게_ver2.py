import heapq

def solution(scoville, k):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < k:
        if len(scoville) == 1:
            count = -1
            break
        else:
            new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            heapq.heappush(scoville, new)
            count += 1
    return count
        
print(solution([1,2,3,9,10,12], 7)) # 2