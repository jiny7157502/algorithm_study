# sentence = input()
# sentence = sentence.strip()

# count = 0
# if sentence != []:
#     count = 1
#     for i in range(len(sentence)):
#         if sentence[i] == " ":
#             count += 1

# print(count)

sentence = input()
sentence = sentence.strip()

array = []
for i in range(len(sentence)):
    array.append(sentence[i])

array.sort()

count = 0

if array != []:
    count = 1
    for i in range(len(array)):
        if array[i] == " ":
            count += 1
        else:
            break

print(count)