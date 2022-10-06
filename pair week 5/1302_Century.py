"""Century"""
def check_be(year):
    """check_be"""
    year = year - 543
    if year <= 0:
        return "ERROR"
    elif year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

def check_ad(year):
    """check_ad"""
    if year <= 0:
        return "ERROR"
    elif year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

def print_ans(num):
    """call func to print ans"""
    for _ in range(num):
        year = input()
        if year[:4] == "B.E.":
            print(check_be(int(year[5:])))
        elif year[:4] == "A.D.":
            print(check_ad(int(year[5:])))
print_ans(int(input()))
