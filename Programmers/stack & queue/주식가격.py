from collections import deque

def solution(prices):
    result = []
    deq = deque(prices)
    while deq:
        item = deq.popleft()
        time = 0
        for i in range(len(deq)):
            if item <= deq[i]:
                time += 1
        result.append(time)
    return result

print(solution([1,2,3,2,3])) # [4,3,1,1,0]