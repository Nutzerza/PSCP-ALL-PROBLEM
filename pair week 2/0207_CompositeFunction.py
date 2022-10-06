"""composite function"""

def func_fx(num):
    """find fx"""
    return 2*num
def func_gx(num):
    """find gx"""
    return num/2+1
def main(num):
    """find all"""
    print("%.2f" %func_fx(func_gx(num)))
    print("%.2f" %func_gx(func_fx(num)))
main(int(input()))
