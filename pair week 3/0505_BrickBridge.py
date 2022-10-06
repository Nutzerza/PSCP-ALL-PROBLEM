"""BrickBridge"""
def main(small, large, want):
    """condition print ans"""
    large_use, small_use = want//5, want%5
    if small + large*5 < want:
        small_use = -1
    elif large - large_use < 0:
        small_use += abs(large - large_use)*5
    elif small < small_use:
        small_use = -1
    else:
        small_use += 0
    print(small_use)
main(int(input()), int(input()), int(input()))
