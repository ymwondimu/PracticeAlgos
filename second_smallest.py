def second_largest(arr):
    max = arr[0]
    second = -float("inf")

    for i in range(0,len(arr)):
        if arr[i] > max:
            second = max
            max = arr[i]
        elif arr[i] > second:
            second = arr[i]

    return second

def second_smallest(arr):
    min = arr[0]
    second = float("inf")

    for i in range(0,len(arr)):
        if arr[i] < min:
            second = min
            min = arr[i]
        elif arr[i] < second:
            second = arr[i]

    return second



def main():
    print (second_smallest([3,8,2,9,-1,100,13]))

if __name__ == "__main__":
    main()