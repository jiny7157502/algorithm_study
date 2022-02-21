num = int(input())

x = 0
y = 0
while True:
    if num % 5 == 0:
        y = num // 5
        break
    else:
        if (num - 3*x) % 5 == 0:
            y = (num - 3*x) // 5
            break
        x += 1

if x < 0 or y < 0:
    print(-1)
else:
    print(x+y)