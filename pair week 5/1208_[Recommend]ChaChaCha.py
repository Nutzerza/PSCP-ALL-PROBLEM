"""[Recommend] Cha Cha Cha"""
def main(num, money_get=0):
    """print ans"""
    for _ in range(num):
        hour_day = float(input())
        if hour_day > int(hour_day):
            hour_day = int(hour_day) + 1
        money_get += 8720 * hour_day
    print(int(money_get))
main(int(input()))
