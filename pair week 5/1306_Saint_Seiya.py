"""Saint Seiya"""
def main(sec, det):
    """print ans"""
    punch = 0
    for counter in range(2, sec+1, 2):
        if punch >= det:
            punch += 12 * (sec - counter + 1)
            break
        elif counter % 6 == 0:
            punch += 1
        elif counter % 2 == 0:
            punch += 165
    print(punch)
main(int(input()), int(input()))
