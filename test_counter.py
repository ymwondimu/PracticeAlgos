from collections import Counter
from collections import defaultdict

def main():
    s = "hello"
    d = defaultdict(int)

    for char in s:
        d[char] += 1

    print (d)
if __name__ == "__main__":
    main()