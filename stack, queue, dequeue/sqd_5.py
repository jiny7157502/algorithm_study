import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    word = sys.stdin.readline().split()
    if word[0] == "push_front":
        array.insert(0, word[1])
        print(array)
    elif word[0] == "push_back":
        array.append(word[1])
        print(array)
    elif word[0] == "pop_front":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
            array.pop(0)
    elif word[0] == "pop_back":
        if len(array) == 0:
            print(-1)
        else:
            print(array[len(array)-1])
            array.pop()
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