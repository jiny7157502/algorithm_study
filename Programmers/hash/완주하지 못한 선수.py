def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# 딕셔너리와 hash() 함수 사용 코드
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += hash(part)
#     for comp in completion:
#         temp -= hash(comp)
#     return dic[temp]

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
