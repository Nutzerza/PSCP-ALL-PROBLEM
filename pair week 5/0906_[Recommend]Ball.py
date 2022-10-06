"""[Recommend] Ball"""
def main(num, counter=0):
    """loop for print ans"""
    while num > 0.01:
        num *= 0.6
        if num >= 0.01:
            counter += 1
    print(counter)
main(float(input()))
