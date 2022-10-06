"""Stamps"""
def main(number_times, total_cost=0, stamp_have=0):
    """print ans"""
    cost_get_stamp = int(input())
    get_stamp = int(input())
    complete_stamp = int(input())
    get_discount = int(input())
    for _ in range(number_times):
        cost = int(input())
        if get_stamp == 0 or get_discount == 0:
            total_cost += cost
        else:
            stamp_promo_use = cost // get_discount
            if cost % get_discount > 0:
                stamp_promo_use += 1

            if stamp_promo_use*complete_stamp <= stamp_have:
                total_cost += 0
                cost_discount = 0
                stamp_have = stamp_have - stamp_promo_use*complete_stamp
            else:
                cost_discount = cost - (stamp_have//complete_stamp)*get_discount
                total_cost += cost_discount
                stamp_have = stamp_have%complete_stamp

            stamp_have += get_stamp * (cost_discount // cost_get_stamp)
    print("%d\n%d" %(total_cost, stamp_have))

main(int(input()))
