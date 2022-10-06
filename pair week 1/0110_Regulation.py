"""Regulation"""


def main(num_x, num_y, txt):
    """print ans"""
    print("%30s" % num_x)
    print(num_x.zfill(30))
    print("%.2f" % num_y)
    print("%.12f" % num_y)
    print("%40s" % txt)


main(input(), float(input()), input())
