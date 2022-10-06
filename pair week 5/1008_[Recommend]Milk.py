"""[Recommend] Milk"""
def find_free_milk(bottle_promo, milk_get, bottle):
    """find free milk"""
    milk = 0
    while bottle >= bottle_promo:
        milk += (bottle // bottle_promo) * milk_get
        bottle = (bottle % bottle_promo) + (bottle // bottle_promo) * milk_get
    return milk

def main(money_for_milk, bottle_promo, milk_get, user_money):
    """print ans"""
    milk = 0
    milk += user_money // money_for_milk
    if bottle_promo == 0 or milk_get == 0:
        print(milk)
    else:
        bottle = milk
        print(milk + find_free_milk(bottle_promo, milk_get, bottle))
main(int(input()), int(input()), int(input()), int(input()))
