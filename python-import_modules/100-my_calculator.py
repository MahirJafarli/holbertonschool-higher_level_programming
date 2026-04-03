#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
