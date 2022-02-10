N = int(input())

for i in range(N):
    num, word = input().split()
    for j in range(len(word)):
        print(int(num)*word[j], end="")
    print()