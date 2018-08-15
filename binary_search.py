import math

def binary_search(arr, low, high, x):
    mid = get_midpoint(low, high)
    if len(arr) == 0:
        return False
    elif len(arr) == 1:
        if arr[0] == x:
            return True
        else:
            return False
    elif arr[mid] == x:
        return True
    elif arr[mid] > x:
        return binary_search(arr[low:mid], low, mid, x)
    elif arr[mid] < x:
        return binary_search(arr[mid:high], mid, high, x)
    return False

def get_midpoint(low, high):
    midpoint = math.floor((high-low)/2)
    return midpoint

def main():
    arr = [2, 3, 5, 8, 12, 16, 18]
    x = 12
    n = len(arr)

    b = binary_search(arr, 0, n, x)
    print (b)


if __name__ == "__main__":
    main()