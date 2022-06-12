N = int(input())
room = 1
count = 1
six = 6
if(N == 1):
    print(1)
else:
    while True:
        count += six
        room += 1
        if N <= count:
            print(room)
            break
        six += 6
