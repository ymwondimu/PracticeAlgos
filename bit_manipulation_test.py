def main():
    print (test("helpo"))


def test(s):
    bit_arr = 0
    for char in s:
        if check_bit(bit_arr, char):
            return False
        else:
            bit_arr = set_bit(bit_arr, char)
    return True


def set_bit(bit_arr, char):
    char_int = int_value(char)

    return bit_arr | (1 << char_int)


def check_bit(bit_arr,char):
    char_int = int_value(char)
    mask = 1 << char_int

    return (bit_arr & mask) > 0


def int_value(char):
    return 26-(ord(char) - ord('a'))


if __name__ == "__main__":
    main()