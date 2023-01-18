def solution(today, terms, privacies):
    today = today.split(".")
    today_year = int(today[0])
    today_month = int(today[1])
    today_day = int(today[2])
    
    answer = []
    for i in range(len(privacies)):
        pri_real = privacies[i].split(" ")
        date = pri_real[0].split(".")
        pri_terms = pri_real[1]
        
        for j in range(len(terms)):
            terms_real = terms[j].split(" ")
            terms_str = terms_real[0]
            terms_value = terms_real[1]
            
            if pri_terms == terms_str:
                real_year = int(date[0])
                real_month = int(date[1]) + int(terms_value)
                real_day = int(date[2])     

                if real_month > 12:
                    real_year = real_year + 1
                    real_month = real_month - 12
                break
            
        # 검사
        print(real_year, real_month, real_day)
        if today_year > real_year:
            answer.append(i+1)
        elif (today_year == real_year and today_month > real_month):
            answer.append(i+1)
        elif (today_year == real_year and today_month == real_month and today_day >= real_day):
            answer.append(i+1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.02", ["Z 12", "D 5"], ["2019.01.01 Z", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))