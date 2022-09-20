def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1
        
        if count < 0:
            return False
    return True if count == 0 else False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))