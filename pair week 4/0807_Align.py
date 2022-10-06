"""Align"""
def main(num, con, txt):
    """print ans"""
    ren = num - len(txt)
    h_ren = int(ren/2)
    if con == "left":
        print(txt + " "*ren)
    elif con == "right":
        print(" "*ren + txt)
    else:
        if ren%2:
            print(" "*(h_ren+1)+txt+" "*h_ren)
        else:
            print(" "*h_ren+txt+" "*h_ren)
main(int(input()), input(), input())
