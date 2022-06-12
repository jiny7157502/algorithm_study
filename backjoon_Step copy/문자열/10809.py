import string

alpha = string.ascii_lowercase

a = input()

for i in alpha:
    print(a.find(i), end=' ')
