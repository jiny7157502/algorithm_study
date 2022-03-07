num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())

    if N // H > 10:
        print(str(N % H) + str(N//H + 1))
    else:        
        print(str(N % H) + str(0) + str(N//H + 1))