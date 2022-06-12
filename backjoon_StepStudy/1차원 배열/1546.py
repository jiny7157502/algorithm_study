n = int(input())
value = []
sum = 0
a = list(map(int, input().split()))
if (len(a) == n):
    for i in range(n):
        value.append(a[i]/max(a)*100)
        sum += value[i]
print(sum/n)
