def compress_string(s):
    if len(s) == 0:
        return ""

    res = ""
    res += s[0]
    count = 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count+=1
        else:
            res+=str(count)
            res+=s[i+1]
            count=1
    res+=str(count)

    print (res)

def main():
    compress_string("aabbbaccc")

if __name__ == "__main__":
    main()