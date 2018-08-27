def highest_avg(student_arr):
    d = {}
    max_avg = -float("inf")
    max_avg_name = ""

    for student in student_arr:
        name = student[0]
        grade = student[1]

        if name not in d:
            d[name] = [grade,1]
            if grade > max_avg:
                max_avg = grade
                max_avg_name = name
        else:
            #print (d[name][0])
            d[name][0] = calculate_average(grade, d[name][0], d[name][1])
            d[name][1] += 1
            if d[name][0] > max_avg:
                max_avg = d[name][0]
                max_avg_name = name

    return (max_avg_name, max_avg)


def calculate_average(grade, prev_avg, count):
    new_avg = ((prev_avg * count) + grade)/(count + 1)
    return new_avg


def main():
    arr = [["jerry", 65], ["bob", 91], ["jerry", 23], ["eric", 83], ["eric", 117]]
    print (highest_avg(arr))


if __name__ == "__main__":
    main()