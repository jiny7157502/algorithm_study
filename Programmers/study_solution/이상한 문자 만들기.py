def solution(s):
    answer = []
    check = 0
    for i in range(len(s)):
        check += 1
        if s[i] == " ":
            answer.append(s[i])
            check = 0
        elif check % 2 == 1:
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    return ''.join(answer)

print(solution("try hello world")) # "TrY HeLlO WoRlD"
print(solution("algorith study")) 
print(solution("banananananananananananana aplle"))
print(solution("APLLE SKDMSKDM"))
print(solution("A A A a A Aaa a AaA"))