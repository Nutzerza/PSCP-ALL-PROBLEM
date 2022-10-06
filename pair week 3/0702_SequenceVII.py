"""Sequence VII"""
def main(num):
    """loop for print"""
    for row in range(1, num+1):
        for col in range(row):
            print(col+1, end=" ")
        print()
    for rev_row in range(num):
        for rev_col in range(num-1-rev_row):
            print(rev_col+1, end=" ")
        print()
main(int(input()))
