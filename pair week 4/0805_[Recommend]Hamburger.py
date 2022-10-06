"""[Recommend] Hamburger"""
def main(front, behind):
    """get value print ans"""
    meat = (front + behind) * 2
    print("|"*front + "*"*meat + "|"*behind)
main(int(input()), int(input()))
