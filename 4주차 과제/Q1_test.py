f = list(map(int, input().split()))
s = list(map(int, input().split()))

fs = []

for i in range(len(f)):
    if (100-f[i]) % s[i] == 0:
        fs.append((100-f[i]) // s[i])
    else:
        fs.append(((100-f[i]) // s[i]) + 1)

count = 0
realCount = []

while fs:
    if len(fs) == 1:
        fs.pop(0)
        count += 1
        realCount.append(count)
        break
    else:
        if fs[0] < fs[1]:
            fs.pop(0)
            count += 1
            realCount.append(count)
            count = 0
        else:
            fs.pop(0)
            count += 1

print(*realCount)