"""Bill"""
def main(cost):
    """print ans"""
    ser_charge = cost * 0.1
    if ser_charge < 50:
        ser_charge = 50
    if ser_charge > 1000:
        ser_charge = 1000
    sum_money = (cost+ser_charge) * 1.07
    print("%.2f" %sum_money)
main(int(input()))
