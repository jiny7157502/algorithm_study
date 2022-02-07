sentence = input()

array = []

for word in sentence:
    if word == "[" or word == "]" or word == "(" or word == ")":
        array.append(word)

real_array = []
check = "yes"
#[]()
for i in range(len(array)):
    if array[i] == "]":
        if len(real_array) == 0:
            check = "no"
            break
        else:
            if real_array[-1] == "[":
                real_array.pop(-1)
            elif real_array[i-1] == ")":
                continue
            else:
                check = "no"
                break
    elif array[i] == ")":
        if len(real_array) == 0:
            check = "no"
            break
        else:
            if real_array[-1] == "(":
                real_array.pop(-1)
            elif real_array[i-1] == "]":
                continue
            else:
                check = "no"
                break
    elif array[i] == "(" or array[i] == "[":
        real_array.append(array[i])

print(check)
