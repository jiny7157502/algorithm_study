def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))