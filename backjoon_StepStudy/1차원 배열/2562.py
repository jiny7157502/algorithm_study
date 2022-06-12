result = 0
a = []
for i in range(9):
    a = int(input())
    if(a > result):
        result = a
        count = i+1
print(result)
print(count)
