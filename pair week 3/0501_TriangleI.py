"""Triangle I"""
def check_sot_side(fir_side, sec_side, thi_side):
    """condition return value"""
    side_1 = side_2 = side_most = 0
    if fir_side >= sec_side and fir_side >= thi_side:
        side_1, side_2, side_most = sec_side, thi_side, fir_side
    elif sec_side >= fir_side and sec_side >= thi_side:
        side_1, side_2, side_most = fir_side, thi_side, sec_side
    elif thi_side >= fir_side and thi_side >= sec_side:
        side_1, side_2, side_most = fir_side, sec_side, thi_side
    return side_1, side_2, side_most

def main(fir_side, sec_side, thi_side):
    """get value print ans"""
    side_1, side_2, side_most = check_sot_side(fir_side, sec_side, thi_side)
    cal_side = side_1**2 + side_2**2
    if 0 <= abs(cal_side - side_most**2) <= 0.01:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()))
