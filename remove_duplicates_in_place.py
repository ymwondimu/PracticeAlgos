def remove_duplicates(arr):
    n = len(arr)
    last_index = 0
    i = 0
    count = 0
    d = {}
    while i < n:
        #print (i)
        num = arr[i]
        #print (i,last_index)
        if num not in d:
            d[num] = 1
            last_index += 1
        else:
            if i+1 < n:
                arr[last_index] = arr[i+1]
                count += 1
                continue
        i+=1

    arr = arr[:-count]

"""i = 5
last_index = 5
count = 1
num = 5

d = [5,12,8,3, 7]
arr = [5,12,8,3,7,12,12,0]"""



def main():
    arr = [5,12,8,5,3,7,12,0]
    remove_duplicates(arr)
    print (arr)


if __name__ == "__main__":
    main()