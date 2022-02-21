num = int(input())

a = 1
b = 1
result = 2
count = 1

while count != num:
    if result % 2 == 0:
        if a == 1:
            result += 1
        b += 1
        a = result - b
    else:
        if b == 1:
            result += 1
        a += 1
        b = result - a
    count += 1

print(str(a) + "/" + str(b))