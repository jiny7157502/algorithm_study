def solution(s):
    if len(s) % 2 == 1:
        answer = s[(len(s)//2)]
    else:
        answer = str(s[(len(s)//2)-1]) + str(s[(len(s)//2)])
    return answer

print(solution("abcde"))
print(solution("qwer"))