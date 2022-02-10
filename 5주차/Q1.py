word = input()
word = word.upper()
unique_word = list(set(word))

count_array = []

for alpha in unique_word:
    count_array.append(word.count(alpha))

if count_array.count(max(count_array)) > 1:
    print("?")
else:
    print(unique_word[count_array.index(max(count_array))])