"""Inflation"""
def main(money, year):
    """print ans"""
    for _ in range(year):
        money += money * 381 // 10000
    print("%d.%02d" %(money//100, money%100))
main(int(float(input()) * 100), int(input()))
