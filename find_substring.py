def find_substring(s, substr):
    n = len(substr)
    start = 0
    end = start + n

    while (end <= len(s)):
        proposed_substring = s[start:end]
        if proposed_substring == substr:
            return True
        start += 1
        end += 1

    return False

def main():
    print (find_substring("hello", "hed"))

if __name__ == "__main__":
    main()