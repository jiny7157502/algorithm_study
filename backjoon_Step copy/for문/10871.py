# N, X = map(int, input().split())
# a = input().split()
# result = []
# if(len(a) != N):
#     print("잘못입력하였습니다.")
# for i in range(len(a)):
#     if(int(a[i]) < X):
#         result.append(a[i])
# for i in range(len(result)):
#     print(result[i], end=' ')

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=' ')
