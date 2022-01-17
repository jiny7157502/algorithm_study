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
            print(array[0])
            array.pop(0)
    elif word[0] == "size":
        print(len(array))
    elif word[0] == "empty":
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == "front":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
    elif word[0] == "back":
        if len(array) == 0:
            print(-1)
        else:
            array.reverse()
            print(array[0])
            array.reverse()