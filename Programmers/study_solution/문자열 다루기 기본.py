def solution(s):
    if len(s) in (4, 6) and s.isdecimal():
        return True
    else:
        return False
    

print(solution("a234"))
print(solution("1234"))
print(solution("12345668"))