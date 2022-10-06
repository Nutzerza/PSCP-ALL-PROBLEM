"""Circular I"""
def main(x_cir, y_cir, radius, x_mos, y_mos):
    """cal num print ans"""
    cal_num = ((x_cir - x_mos)**2 + (y_cir - y_mos)**2)**0.5
    if cal_num > radius:
        print("No")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
