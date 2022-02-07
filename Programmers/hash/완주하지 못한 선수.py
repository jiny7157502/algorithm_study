def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

print(hash())