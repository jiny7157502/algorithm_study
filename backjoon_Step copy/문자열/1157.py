# word = input().upper()
# unique_word = list(set(word))
# cnt_word = []
# for i in unique_word:
#     cnt = word.count(i)
#     cnt_word.append(cnt)
# print(cnt_word)
# if cnt_word.count(max(cnt_word)) > 1:
#     print("?")
# else:
#     max_index = cnt_word.index(max(cnt_word))
#     print(unique_word[max_index])

# str = input().upper()
# unique_str = list(set(str))
# cnt = []
# for i in unique_str:
#     cnt_str = str.count(i)
#     cnt.append(cnt_str)
# if cnt.count(max(cnt)) > 1:
#     print("?")
# else:
#     max_index = cnt.index(max(cnt))
#     print(unique_str[max_index])

word = input().upper()
unique_word = list(set(word))

word_count = []
for i in unique_word:
    count = word.count(i)
    word_count.append(count)
if word_count.count(max(word_count)) > 1:
    print("?")
else:
    max_index = word_count.index(max(word_count))
    print(unique_word[max_index])
