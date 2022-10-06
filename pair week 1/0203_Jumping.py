"""Jumping"""


def jumping():
    """call function"""
    print_output(1)
    print_output(2)
    print_output(3)
    print_output(4)


def print_output(num):
    """function output"""
    for _ in range(3):
        print("Output"+str(num))


jumping()
