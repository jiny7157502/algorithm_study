n = int(input())
a = list(map(int, input().split()))
if(len(a) == n):
    print(min(a), max(a))
