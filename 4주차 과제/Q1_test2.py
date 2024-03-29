def solution(progresses, speeds):
    time = 0
    count = 0
    answer = []
    while len(progresses) > 0:
        if progresses[0] + speeds[0] * time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    print(answer)
    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])