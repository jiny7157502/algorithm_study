from collections import deque

def solution(priorities, location):
    result = 0
    
    deq = deque([(v, i) for i, v in enumerate(priorities)]) # [(2, 0), (1, 1), (3, 2), (2, 3)]
    
    while len(deq):
        item = deq.popleft()
        
        if deq and item[0] < max(deq)[0]:
            deq.append(item)
        else:
            result += 1
            if location == item[1]:
                break
    return result

print(solution([2, 1, 3, 2], 0))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 1