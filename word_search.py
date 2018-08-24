def check_word(puzzle, word):
    x = len(puzzle)
    y = len(puzzle[0])

    for row in range(x):
        for col in range(y):
            found_right = search_right(puzzle, word, row, col)
            if found_right:
                print ("Found scanning to the right")
                print ("Row Start Index: " + str(row) + "\tColumn Start Index: " + str(col))
                return True
            found_down = search_down(puzzle, word, row, col)
            if found_down:
                print("Found scanning downwards")
                print("Row Start Index: " + str(row) + "\tColumn Start Index: " + str(col))
                return True
            found_diagonal = search_right_down(puzzle, word, row, col)
            if found_diagonal:
                print("Found scanning diagonally down and to the right")
                print("Row Start Index: " + str(row) + "\tColumn Start Index: " + str(col))
                return True
    return False

def make_puzzle(arr):
    output = []
    for val in arr:
        output.append(list(val))

    return output

def search_right(puzzle, word, row_start, col_start):
    for i in range(len(word)):
        col_index = col_start + i
        if col_index > len(puzzle[0]):
            return False
        else:
            if puzzle[row_start][col_index] != word[i]:
                return False

    return True

def search_down(puzzle, word, row_start, col_start):
    for i in range(len(word)):
        row_index = row_start + i
        if row_index > len(puzzle):
            return False
        else:
            #print (row_index, col_start)
            if puzzle[row_index][col_start] != word[i]:
                return False
    return True

def search_right_down(puzzle, word, row_start, col_start):
    for i in range(len(word)):
        row_index = row_start + i
        col_index = col_start + i
        if row_index >= len(puzzle) or col_index >= len(puzzle[0]):
            return False
        else:
            if puzzle[row_index][col_index] != word[i]:
                return False
            else:
                print (puzzle[row_index][col_index])

    return True

def main():
    arr = ["batae", "eliau", "awetj", "rodsl", "suqno"]
    puzzle = make_puzzle(arr)
    print (check_word(puzzle, ""))

if __name__ == "__main__":
    main()



