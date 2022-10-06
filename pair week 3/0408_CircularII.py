"""Circular II"""
def main():
    """get valuse print ans"""
    x_cir_one, y_cir_one, radius_one = float(input()), float(input()), float(input())
    x_cir_two, y_cir_two, radius_two = float(input()), float(input()), float(input())
    cal_num = ((x_cir_one - x_cir_two)**2 + (y_cir_one - y_cir_two)**2)**0.5
    if cal_num >= radius_one + radius_two:
        print("No")
    else:
        print("Yes")
main()
