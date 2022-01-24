import sys

N = int(sys.stdin.readline())

for i in range(N):
    n, m = map(int, sys.stdin.readline().split(" "))
    array = list(sys.stdin.readline().split(" "))
    
    count = 0

    if(len(array) == n):
        array[n-1] = array[n-1].rstrip()
        for j in range(m, n):
            if j == n-1:
                count += 1
            elif array[j] <= array[j+1]:
                count += 1
        print(count)
    else:
        print("입력한 n의 개수와 맞지 않음")
        break
