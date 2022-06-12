import string
alphabet = string.ascii_uppercase


def Solution(nameList):
    name_list = list(nameList.split(', '))
    real_list = sorted(set(name_list))
    final_list = []
    count = [0] * len(real_list)

    arr = [[0] * 3 for _ in range(3)]
    print(arr)

    for i in range(len(name_list)):
        for j in range(len(real_list)):
            if(name_list[i] == real_list[j]):
                final_list.append(name_list[i]+alphabet[count[j]])
                count[j] += 1
    print(final_list)

    for name in name_list:
        for j in range(len(real_list)):
            if(name == real_list[j]):
                final_list.append(name+alphabet[count[j]])
                count[j] += 1
    print(final_list)


if __name__ == '__main__':
    nameList = ["김바바", "김바바", "이바바", "김토스", "이바바", "김바바"]
    Solution("김바바, 김바바, 이바바, 김토스, 이바바, 김바바")
