def merge_intervals(intervals):
    sorted_interval = sorted(intervals, key=lambda x: x[0])
    merged = []

    for interval in sorted_interval:
        if not merged:
            merged.append(interval)
        else:
            previous_interval = merged.pop()
            if previous_interval[1] >= interval[0]:
                new_interval = (previous_interval[0], max(previous_interval[1], interval[1]))
                merged.append(new_interval)
            else:
                merged.append(previous_interval)
                merged.append(interval)
    return merged


def main():
    print (merge_intervals([(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]))


if __name__ == "__main__":
    main()