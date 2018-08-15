def isPalindrome(n):
    num = n
    reversed_digit = 0

    while (num>0):
        digit = num%10
        reversed_digit=reversed_digit*10 + digit
        num = num//10

    print (n, reversed_digit)

    if reversed_digit == n:
        return True
    else:
        return False

def main():
    print (isPalindrome(121))
    print (isPalindrome(123))
    print (isPalindrome(5))

if __name__ == "__main__":
    main()