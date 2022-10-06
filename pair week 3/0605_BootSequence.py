"""BootSequence"""
def main(num):
    """print ans"""
    for count in range(1, num+1):
        if count == num:
            print(count)
        else:
            print(count, end="_")
main(int(input()))
