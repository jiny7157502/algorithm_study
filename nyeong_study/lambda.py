# def hap(x, y):
#     return print(x+y)

# hap(10, 20)

# lambda 매개변수 : 표현식

# result = (lambda a,b : a + b)(10, 20)
# print(result)

# 2차원 배열 정렬
# key -> 함수의 결과에 따라 정렬할 수 있음

# 첫 번째 값으로 정렬
array = [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]
array.sort(key=lambda x:x[0])
print(array)
# 결과값 : [[1, 2], [1, 3], [2, 1], [3, 4], [3, 2]]

# 두 번째 값으로 정렬 -> x : ()의 괄호안의 튜플 형태로 넣음
# array = [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]
# array.sort(key=lambda x : (x[1], x[0]))
# print(array)
# 결과값 : [[2, 1], [1, 2], [3, 2], [1, 3], [3, 4]]