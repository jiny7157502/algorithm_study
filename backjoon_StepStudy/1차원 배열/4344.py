c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    sum = 0
    avg = 0
    count = 0
    for i in range(1, len(n)):
        sum += int(n[i])
        avg = sum / (len(n)-1)
    for i in range(1, len(n)):
        if avg < int(n[i]):
            count += 1
    print('%.3f' % (count/(len(n)-1)*100) + "%")
