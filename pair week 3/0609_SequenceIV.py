"""Sequence IV"""
def main(num):
    """loop for print ans"""
    counter = 1
    for _ in range(num):
        for _ in range(num):
            print(counter, end=" ")
            counter += 1
        print()
main(int(input()))
