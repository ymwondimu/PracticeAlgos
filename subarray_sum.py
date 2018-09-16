def subarray_sum(arr, x):
    n = len(arr)
    curr_sum = arr[0]
    start = 0

    i = 1
    while i <= n:

        while curr_sum > x and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == x:
            return arr[start:i]

        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    print ("None Found")
    return 0


def main():
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    x = 23
    print (subarray_sum(arr,x))

if __name__ == "__main__":
    main()