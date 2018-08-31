def one_edit(s1, s2):
    return is_replaced(s1,s2) or is_deleted(s1, s2) or is_added(s1,s2)


def is_replaced(s1, s2):
    if len(s1) != len(s2):
        return False

    count = 0
    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]

        if char1 != char2:
            count += 1

    if count == 1:
        return True
    else:
        return False


def is_deleted(s1, s2):
    if len(s2) != len(s1) - 1:
        return False

    index1 = 0
    index2 = 0
    count = 0

    while index1 < len(s1):
        char1 = s1[index1]
        char2 = s2[index2]

        if char1 != char2:
            index1 += 1
            count += 1
        else:
            index1 += 1
            index2 += 1

    if count == 1:
        return True
    else:
        return False


def is_added(s1,s2):
    if len(s2) != len(s1) + 1:
        return False

    index1 = 0
    index2 = 0
    count = 0

    while index2 < len(s2):
        char1 = s1[index1]
        char2 = s2[index2]

        if char1 != char2:
            index2 += 1
            count += 1
        else:
            index1 += 1
            index2 += 1

    if count == 1:
        return True
    else:
        return False


def main():
    print (one_edit("hello", "hellpo"))
    print (one_edit("helpo", "hello"))
    print (one_edit("hello", "helo"))
    print (one_edit("aaaaa", "aaab"))


if __name__ == "__main__":
    main()