from collections import Counter

def delete_characters(str, remove):
    d = Counter(remove)
    output = ""
    for char in str:
        if char not in d:
            output += char

    return output

def main():
    print (delete_characters("Battle of the Vowels: Hawaii vs. Grozny", "aeiou"))

if __name__ == "__main__":
    main()