def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    match = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    print (match)
    match[0][0] = True
    for i in range(1, len(s1) + 1):
        match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, len(s2) + 1):
        match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                          or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    return match[-1][-1]


def main():
    c = "abcdef"
    a = "abd"
    b = "def"
    print (isInterleave(a, b, c))

if __name__ == "__main__":
    main()
