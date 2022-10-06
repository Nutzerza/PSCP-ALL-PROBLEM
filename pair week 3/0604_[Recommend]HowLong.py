"""[Recommend] HowLong"""
def how_long(txt):
    """sum quantity"""
    quantity = 0
    for _ in txt:
        quantity += 1
    return quantity

def main(num):
    """get value"""
    print(how_long(str(abs(num))))
main(int(input()))
