# Uses python3
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    fib_list = [0] * n
    fib_list[1] = 1
    for i in range(2, len(fib_list)):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

    return fib_list[-1]


n = int(input())
print(calc_fib(n))
