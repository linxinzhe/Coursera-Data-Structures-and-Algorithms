# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    if a < b:
        a, b = b, a

    while True:
        if b == 1:
            return 1

        if b == 0:
            current_gcd = a
            break

        a, b = b, a % b

    return current_gcd


def lcm_naive(a, b):
    gcd = gcd_naive(a, b)

    return a * b // gcd


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
