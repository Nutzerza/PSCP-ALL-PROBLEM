"""WeightStation"""
def main(avg_weight, fir_weight, sec_weight, thi_weight):
    """get valuse condition print ans"""
    fou_weight = 4*avg_weight - (fir_weight + sec_weight + thi_weight)
    sum_weight = fir_weight + sec_weight + thi_weight + fou_weight

    percent_fir, percent_sec = fir_weight / avg_weight, sec_weight / avg_weight
    percent_thi, percent_fou = thi_weight / avg_weight, fou_weight / avg_weight
    if sum_weight > 15000:
        print("Overweight")

    elif percent_fir > 1.5 or percent_fir < 0.5 or percent_sec > 1.5 or percent_sec < 0.5 or \
        percent_thi > 1.5 or percent_thi < 0.5 or percent_fou > 1.5 or percent_fou < 0.5:
        print("Unbalance")

    else:
        print("Pass %.2f" %fou_weight)

main(float(input()), float(input()), float(input()), float(input()))
