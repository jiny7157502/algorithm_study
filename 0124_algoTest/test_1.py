import sys

N = int(sys.stdin.readline())

# array 입력받는 코드 및 마지막 줄바꿈 처리
array = list(sys.stdin.readline().split(" "))
array[len(array)-1] = array[len(array)-1].rstrip() 

final_data = []

# N과 array의 길이가 같은 경우
if len(array) == N:
    for i in range(N):
        # 마지막 원소인 경우 -1 출력
        if i == N-1:
            final_data.append(-1)
            break
        # 마지막 원소가 아닌 경우
        else:
            for j in range(i+1, N):
                # i+n 위치의 값이 i 위치의 값보다 큰 경우 
                if array[j] > array[i]:
                    final_data.append(array[j]) 
                    break
                # i+n 위치의 값이 i 위치의 값보다 큰 값이 없는 경우
                else:
                    if j+1 == len(array):
                        final_data.append(-1)
                        break
# N과 array의 길이가 다른 경우
else:
    print("원소의 개수를 확인하세요")

for data in final_data:
    print(data, end = " ")

