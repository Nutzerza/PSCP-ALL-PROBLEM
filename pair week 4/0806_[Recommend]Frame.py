"""[Recommend] Frame"""
def main(txt):
    """print ans"""
    length = len(txt) + 2
    print("*"*length, "*%s*" %txt, "*"*length, sep="\n")
main(input())
