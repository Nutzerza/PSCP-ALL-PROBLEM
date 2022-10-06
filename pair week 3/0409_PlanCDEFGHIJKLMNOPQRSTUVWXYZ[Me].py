"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def check_ascend(st_num, nd_num, th_num):
    """check ascend and return txt"""

    most_num = mid_num = low_num = 0

    if st_num > nd_num and st_num > th_num:
        most_num = st_num
        if nd_num > th_num:
            mid_num, low_num = nd_num, th_num
        else:
            mid_num, low_num = th_num, nd_num

    elif nd_num > st_num and nd_num > th_num:
        most_num = nd_num
        if st_num > th_num:
            mid_num, low_num = st_num, th_num
        else:
            mid_num, low_num = th_num, st_num

    else:
        most_num = th_num
        if nd_num > st_num:
            mid_num, low_num = nd_num, st_num
        else:
            mid_num, low_num = st_num, nd_num

    txt = "%.2f, %.2f, %.2f" %(low_num, mid_num, most_num)
    return txt

def check_descend(st_num, nd_num, th_num):
    """check descend and return txt"""

    most_num = mid_num = low_num = 0

    if st_num > nd_num and st_num > th_num:
        most_num = st_num
        if nd_num > th_num:
            mid_num, low_num = nd_num, th_num
        else:
            mid_num, low_num = th_num, nd_num

    elif nd_num > st_num and nd_num > th_num:
        most_num = nd_num
        if st_num > th_num:
            mid_num, low_num = st_num, th_num
        else:
            mid_num, low_num = th_num, st_num

    else:
        most_num = th_num
        if nd_num > st_num:
            mid_num, low_num = nd_num, st_num
        else:
            mid_num, low_num = st_num, nd_num

    txt = "%.2f, %.2f, %.2f" %(most_num, mid_num, low_num)
    return txt

def main(desire):
    """get value print ans"""
    st_num, nd_num, th_num = float(input()), float(input()), float(input())
    if desire == "Ascend":
        print(check_ascend(st_num, nd_num, th_num))
    if desire == "Descend":
        print(check_descend(st_num, nd_num, th_num))
main(input())
