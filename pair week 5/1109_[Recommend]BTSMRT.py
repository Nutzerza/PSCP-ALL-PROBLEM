"""[Recommend] BTSMRT"""
def main(day, age, high):
    """get value print ans"""
    con_1 = day == "Children Day" and age < 14 and high <= 140
    con_2 = age < 14 and high < 90
    con_3 = day == "Senior Day" and age >= 60
    if con_1 or con_2 or con_3:
        print("FREE")
    else:
        print("PAY")
main(input(), float(input()), float(input()))
