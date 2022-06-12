n = int(input())
count = 0
for i in range(1, n+1):
    if i <= 99:
        count += 1
    else:
        n2 = list(map(int, str(i)))
        if n2[0] - n2[1] == n2[1] - n2[2]:
            count += 1
print(count)
