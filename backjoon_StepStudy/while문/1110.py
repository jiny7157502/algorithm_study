n = int(input())
result = 0
count = 0
while (True):
    if n < 10:
        n = int(str(n) + str(0))
    if(count == 0):
        result = int(str(n % 10) + str(((n//10) + (n % 10)) % 10))
    else:
        result = int(str(result % 10) +
                     str(((result//10) + (result % 10)) % 10))
    count += 1
    if result == n:
        break
print(count)
