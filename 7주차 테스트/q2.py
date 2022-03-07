import math

def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)):
        if i+1 >= math.ceil(len(citations)/2):
            answer = citations[i]
            break            
    return answer

print(solution([3,0,6,1,5]))