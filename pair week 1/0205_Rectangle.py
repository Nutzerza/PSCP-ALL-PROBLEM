"""Rectangle"""
def area(width, length):
    """cal&print area"""
    print(width*length)

def circumference(width, length):
    """cal&print circumference"""
    print((width+length)*2)

def main(width, length):
    """call function"""
    area(width, length)
    circumference(width, length)
main(int(input()), int(input()))
