# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd(a, b):
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


def lcm(a, b):
    gcd_num = gcd(a, b)

    return a * b // gcd_num


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
