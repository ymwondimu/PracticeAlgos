from collections import defaultdict

def main():
    print (first_nonrepeating(""))

def first_nonrepeating(s):
    if len(s) == 0:
        return None
    d = defaultdict(int)
    for char in s:
        d[char] += 1

    for i, char in enumerate(s):
        if d[char] == 1:
            return i

    return None


if __name__ == "__main__":
    main()