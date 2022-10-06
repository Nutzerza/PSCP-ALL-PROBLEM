"""Align"""
def main(num, condition, txt):
    """print ans"""
    ren = num - len(txt)
    if condition == "left":
        print(txt + " "*(ren))
    elif condition == "center":
        if ren % 2 == 0:
            print(" "*int(ren/2) + txt + " "*int(ren/2))
        else:
            print(" "*int((ren/2)+1) + txt + " "*int(ren/2))
    elif condition == "right":
        print(" "*(ren) + txt)
main(int(input()), input(), input())
