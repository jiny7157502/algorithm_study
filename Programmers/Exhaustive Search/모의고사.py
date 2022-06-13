def solution(answers):
    answer = []
    
    su_1 = [1,2,3,4,5]
    su_2 = [2,1,2,3,2,4,2,5]
    su_3 = [3,3,1,1,2,2,4,4,5,5]
    
    count = [0,0,0]
    
    for i in range(len(answers)):
        if su_1[i%5] == answers[i]:
            count[0] += 1
        if su_2[i%8] == answers[i]:
            count[1] += 1
        if su_3[i%10] == answers[i]:
            count[2] += 1
    
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
    
    return answer


answers = [1,3,2,4,2]
print(solution(answers))