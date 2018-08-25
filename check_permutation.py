from collections import Counter

def check_permutation(s1,s2):
    if len(s1) != len(s2):
        return False

    d = Counter(s1)

    for char in s2:
        if char not in d:
            return False
        else:
            if d[char] <= 0:
                return False
            else:
                d[char] -= 1
    return True

def main():
    print (check_permutation("yeab", "baey"))
    print (check_permutation("yeab", "able"))


if __name__ == "__main__":
    main()