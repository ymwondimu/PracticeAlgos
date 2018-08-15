def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    a = 0
    b = 1

    for i in range(n):
        a,b = b, a+b

    return a


def main():
    res = fib_recursive(5)
    res2 = fib_iterative(5)
    print (res)
    print (res2)

if __name__ == "__main__":
    main()