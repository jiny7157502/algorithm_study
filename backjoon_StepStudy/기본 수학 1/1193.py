X = int(input())

A = 1
B = 0
count = 0
num = 2
while True:
    B = num - A
    if(B == 0):
        num += 1
        A = 1
    else:
        count += 1
        if count == X:
            if ((num % 2) != 0):
                print(str(A) + "/" + str(B))
                break
            else:
                print(str(B) + "/" + str(A))
                break
        A += 1
