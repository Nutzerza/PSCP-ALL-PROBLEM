"""Left Arrow"""
def main(num_col, num_row):
    """loop for print"""
    count = int((num_row-1)/2)
    for num in range(num_row):
        print(" "*(count) + "*"*num_col)
        if num >= (num_row-1)/2:
            count += 1
        elif num < (num_row-1)/2:
            count -= 1
main(int(input()), int(input()))
