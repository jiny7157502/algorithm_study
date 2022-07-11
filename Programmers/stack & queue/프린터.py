from collections import deque

def solution(priorities, location):
    answer = 0
    
    document = deque([(v, i) for i, v in enumerate(priorities)]) # (2, 0), (1, 1), (3, 2), (2, 3)
    
    while len(document):
        item = document.popleft()
        if document and max(document)[0] > item[0]:
            document.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    
    return print(answer)

solution([2,1,3,2], 2)