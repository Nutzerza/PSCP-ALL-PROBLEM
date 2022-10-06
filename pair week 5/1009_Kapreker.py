"""Kaprekar"""
def most_num(num):
    """return most num"""
    return_num = ""
    for counter in range(9, -1, -1):
        if str(counter) in num:
            return_num += str(counter)
        if num.count(str(counter)) > 1: #กันเลขซ้ำ
            return_num += str(counter)*(num.count(str(counter))-1)
    return int(return_num)

def lowest_num(num):
    """return lowest num"""
    return_num = ""
    for counter in range(0, 10):
        if str(counter) in num:
            return_num += str(counter)
        if num.count(str(counter)) > 1: #กันเลขซ้ำ
            return_num += str(counter)*(num.count(str(counter))-1)
    return int(return_num)

def main(num, total=0):
    """print ans"""
    while num != "6174":
        # print(str(most_num(num) - lowest_num(num)).zfill(4))
        num = str(most_num(num) - lowest_num(num)).zfill(4)
        total += 1
    print(total)
main(input().zfill(4))
