while True:
    sentence = input()

    real_array = []

    temp = True

    if sentence == ".":
        break

    for i in range(len(sentence)):
        if sentence[i] == "]":
            if not real_array or real_array[-1] == '(':
                temp = False
                break
            else:
                if real_array[-1] == "[":
                    real_array.pop(-1)
        elif sentence[i] == ")":
            if not real_array or real_array[-1] == '[':
                temp = False
                break
            else:
                if real_array[-1] == "(":
                    real_array.pop(-1)
        elif sentence[i] == "(" or sentence[i] == "[":
            real_array.append(sentence[i])
    if temp == True and not real_array:
        print('yes')
    else:
        print('no')
