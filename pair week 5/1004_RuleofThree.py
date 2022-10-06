"""RuleofThree"""
def good_value(fir_cost, fir_weight, sec_cost, sec_weight):
    """check good_value"""
    cal_fir = fir_weight / fir_cost
    cal_sec = sec_weight / sec_cost
    if cal_fir > cal_sec:
        return fir_cost, fir_weight
    if cal_fir < cal_sec:
        return sec_cost, sec_weight
    if cal_fir == cal_sec:
        if fir_cost > sec_cost:
            return sec_cost, sec_weight
        else:
            return fir_cost, fir_weight

def main(num):
    """print ans"""
    fir_cost, fir_weight = float(input()), float(input())
    for _ in range(num-1):
        sec_cost, sec_weight = float(input()), float(input())
        fir_cost, fir_weight = good_value(fir_cost, fir_weight, sec_cost, sec_weight)
    print("%.2f %.2f" %(fir_cost, fir_weight))
main(int(input()))
