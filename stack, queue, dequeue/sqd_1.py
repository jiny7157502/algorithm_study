import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    word = sys.stdin.readline().split()

    if word[0] == "push":
        array.append(word[1])
    elif word[0] == "pop":
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])
            array.pop()
    elif word[0] == "size":
        print(len(array))
    elif word[0] == "empty":
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == "top":
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])
