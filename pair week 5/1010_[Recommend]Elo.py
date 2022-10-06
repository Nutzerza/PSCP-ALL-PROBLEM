"""[Recommend] Elo"""
def cal_ea(num_ra, num_rb):
    """cal Ea"""
    return 1/(1+(10**((num_rb - num_ra)/400)))

def cal_eb(num_ra, num_rb):
    """cal Eb"""
    return 1/(1+(10**((num_ra - num_rb)/400)))

def main(num_ra, num_rb, condition):
    """print ans"""
    if condition == "A":
        print("%.2f" %cal_ea(num_ra, num_rb))
    else:
        print("%.2f" %cal_eb(num_ra, num_rb))
main(int(input()), int(input()), input())
