# def solution(s):
#     p_cnt, y_cnt = 0
#     for i in s:
#         if i == "P" or i == "p":
#             p_cnt += 1
#         if i == "Y" or i == "y":
#             y_cnt += 1
#     return p_cnt == y_cnt

def solution(s):
    return s.lower().count('p') == s.lower().count('y')    

print(solution("pPoooyY"))
print(solution("Pyy"))