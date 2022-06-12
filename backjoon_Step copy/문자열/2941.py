cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro_word:
    word = word.replace(i, "*")

print(len(word))
