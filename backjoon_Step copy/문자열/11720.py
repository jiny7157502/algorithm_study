n = int(input())
a = input()
sum = 0
if(len(a) == n):
    for i in range(n):
        sum += int(a[i])
print(sum)
