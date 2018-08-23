def saturation(ranges):
    max = -float("inf")
    min = float("inf")
    for val in ranges:
        if val[0] < min:
            min = val[0]
        if val[1] > max:
            max = val[1]

    arr = [0]*(max-min+1)
    for val in ranges:
        for i in range(val[0], val[1]+1):
            arr[i] += 1

    print (arr)

    prev = None
    count = 0
    for i in range(len(arr)):
        if prev != arr[i]:
            count = 0
        if arr[i] == 0:
            return False
        elif arr[i] > 1:
            if count > 0:
                return False
            else:
                count += 1
        prev = arr[i]

    return True

def main():
    ranges = [[0, 4], [2, 10], [11, 15]]
    print (saturation(ranges))

if __name__ == "__main__":
    main()


