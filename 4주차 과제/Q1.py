f = list(map(int, input().split()))
s = list(map(int, input().split()))

fs = []

print(f)
print(s)

for i in range(len(f)):
    if (100-f[i]) % s[i] == 0:
        fs.append((100-f[i]) // s[i])
    else:
        fs.append(((100-f[i]) // s[i]) + 1)

countList = []

count = 0

for i in range(len(fs)):
    if i == len(fs)-1:
        count += 1
        countList.append(count)
        break
    else:
        if fs[i] < fs[i+1]:
            count += 1
            countList.append(count)
            count = 0
        else:
            count += 1

print(*countList)