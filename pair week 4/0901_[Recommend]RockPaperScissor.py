"""[Recommend] RockPaperScissor"""
def main(txt):
    """print ans"""
    score_a = score_b = 0

    for num in range(0, len(txt), 2):
        if txt[num:num+2] == "RS" or txt[num:num+2] == "PR" or txt[num:num+2] == "SP":
            score_a += 1
        elif txt[num:num+2] == "SR" or txt[num:num+2] == "RP" or txt[num:num+2] == "PS":
            score_b += 1

    if score_a == score_b:
        print("DRAW", score_a)
    elif score_a > score_b:
        print("A win %d-%d" %(score_a, score_b))
    elif score_b > score_a:
        print("B win %d-%d" %(score_b, score_a))

main(input())
