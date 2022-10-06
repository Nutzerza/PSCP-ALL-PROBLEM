"""Sequence VIII"""
def main(num):
    """loop for print ans"""
    for row in range(1, num+1):
        counter = 1
        for col in range(num):
            if col >= num - row:
                print(str(counter).zfill(2), end=" ")
                counter += 1
            else:
                print("  ", end=" ")
        print()
main(int(input()))
