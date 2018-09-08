def reverse(s):
    s = s.strip()
    arr = list(s)
    n = len(arr)

    for i in range(n):
        j = n-i-1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        else:
            break
    return ''.join(arr)



def main():
    print (reverse("hello"))


if __name__ == "__main__":
    main()