def saturated(ranges):
    sorted_ranges = sort(ranges)

    for i in range(len(sorted_ranges)-1):
        range1 = sorted_ranges[i]
        range2 = sorted_ranges[i+1]

        diff = range2[0] - range1[1]

        if diff > 1 or diff < 0:
        #if diff != 1:
           return False

    return True


def sort(ranges):
    final = sorted(ranges, key=lambda x: x[0])
    print (final)
    return final

def main():
    ranges = [[-5, -2], [-1, 0], [3,5], [1,2], [10,15], [6,9]]
    ranges2 = [[3,10], [0,5], [50,100]]
    print (saturated(ranges))

if __name__ == "__main__":
    main()