"""[Recommend] Restaurant"""
def main(cost, cost_promo, discount, want):
    """Print ans"""
    sum_cost_want = cost + want
    cost_discount = cost * (1-discount/100)
    cost_want_discount = sum_cost_want*(1-discount/100)
    if cost == cost_promo and cost_discount < cost_want_discount:
        print("No %.3f" %(cost_want_discount-cost_discount))
    elif cost == cost_promo and cost_discount > cost_want_discount:
        print("Yes %.3f" %(cost_discount-cost_want_discount))
    elif cost_want_discount > cost:
        print("No %.3f" %(cost_want_discount-cost))
    elif cost_want_discount < cost:
        print("Yes %.3f" %(cost-cost_want_discount))
    elif cost_want_discount == cost:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
