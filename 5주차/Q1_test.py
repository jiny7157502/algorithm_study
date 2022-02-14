import string

array = [-1]*26
alphabet = string.ascii_lowercase

word = input()

for i in range(len(word)):
    if word.find(word[i]) != -1:
        index = alphabet.find(word[i])
        array[index] = word.find(word[i])

print(" ".join(map(str, array)))