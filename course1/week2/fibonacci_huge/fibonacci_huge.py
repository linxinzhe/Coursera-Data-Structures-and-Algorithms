# Uses python3
import sys
import operator


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    fib_list = []
    mod_list = []
    mod_period_list = []

    previous = 0
    current = 1

    for _ in range(n - 1):
        fib_list.append(previous)
        mod_list.append(previous % m)

        if not mod_period_list and len(mod_list) % 2 == 0:
            half_index = len(mod_list) // 2

            former_part = mod_list[:half_index]
            later_part = mod_list[half_index:]
            if operator.eq(former_part, later_part):
                mod_period_list = former_part
                break

        previous, current = current, previous + current

    if mod_period_list:
        reminder = n % len(mod_period_list)
        return mod_period_list[reminder]

    # print(fib_list)
    # print(mod_list)
    # print(mod_period_list)
    return current % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # n, m = 2816213588, 30524
    print(get_fibonacci_huge(n, m))
