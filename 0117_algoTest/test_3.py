import sys

N = int(sys.stdin.readline())

array = []

final_data = []

array = list(sys.stdin.readline().split(" "))

if(len(array) == N):

    array[N-1] = array[N-1].rstrip()

    for i in range(N):
        if i == N-1:
            final_data.append(-1)
            break
        for j in range(i+1, N):
            if array[i] < array[j]:
                final_data.append(array[j])
                break
            else:
                if j+1 == len(array):
                    final_data.append(-1)
                    break
else:
    print("입력한 개수가 맞지 않음")

for data in final_data:
    print(data, end=" ")