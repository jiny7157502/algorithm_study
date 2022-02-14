croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input() # ljes=njak
count = 0

for i in range(len(croatia)):
    print(word.find(croatia[i]))
    if word.find(croatia[i]) != -1:
        count += 1
        word = word.replace(croatia[i], "")

print(len(word) + count) # 6