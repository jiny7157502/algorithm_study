def solution(s, n):
    answer = []
    for i in s:
        if i == " ":
            answer.append(" ")
        elif ord(i) + n > 122 or (ord(i) + n > 90 and ord(i) < 91):
            answer.append(chr(ord(i) + n - 26))
        else:
            answer.append(chr(ord(i) + n))
    return "".join(answer)

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

print(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1))
