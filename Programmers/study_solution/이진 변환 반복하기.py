def solution(s):
    zero_cnt = 0
    result_cnt = 0
    while s != "1":
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = "{0:b}".format(len(s))
        result_cnt += 1
    return [result_cnt, zero_cnt]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))