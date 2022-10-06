"""PointInCircle"""
def main(num_x, num_y, num_r, num_xn, num_yn):
    """condition print ans"""
    numx_square = (num_xn-num_x)**2
    numy_square = (num_yn-num_y)**2
    if numx_square+numy_square <= num_r**2:
        print("True")
    else:
        print("False")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
