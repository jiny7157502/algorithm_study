# n : 전체 학생 수, lost : 체육복을 잃어버린 학생의 번호, reverse : 여벌의 체육복을 가진 학생의 번호

def solution(n, lost, reserve):
    
    set_reserve = set(reserve) -set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

print(solution(5, [2,4], [1,3,5])) # 5
print(solution(5, [2,4], [3]))     # 4
print(solution(3, [3], [1]))       # 2
