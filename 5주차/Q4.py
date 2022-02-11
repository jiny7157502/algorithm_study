num = ["ABC", "DEF", "GHI", "JKL" ,"MNO", "PQRS", "TUV", "WXYZ"]

word = input()

sum = 0
for i in range(len(word)):
    for j in range(len(num)):
        if num[j].find(word[i]) != -1:
            sum += j + 3

print(sum)