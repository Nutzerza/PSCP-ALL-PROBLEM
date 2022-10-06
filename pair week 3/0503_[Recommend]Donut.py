"""[Recommend] Donut"""
def main(price, amount_promo, free, want):
    """condition print ans"""
    all_donut = all_price = 0
    amount = amount_promo + free
    num, scrap = want // amount, want % amount
    if num > 0:
        all_price += ((num*amount)-(num*free))*price
        all_donut += num*amount
    if scrap >= amount_promo:
        all_donut += ((scrap//amount_promo)*amount_promo)+free
        all_price += ((scrap//amount_promo)*amount_promo)*price
    if scrap < amount_promo:
        all_donut += scrap
        all_price += scrap*price
    print(all_price, all_donut)
main(int(input()), int(input()), int(input()), int(input()))
