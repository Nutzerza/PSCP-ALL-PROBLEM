"""Lotto"""
def main(sum_money=0):
    """print ans"""
    reward_first = input()
    reward_2last = input()
    reward_31first = input()
    reward_32first = input()
    reward_31last = input()
    reward_32last = input()

    user_lot = input()
    if user_lot[4:6] == reward_2last:
        sum_money += 2000
    if user_lot[0:3] == reward_31first:
        sum_money += 4000
    if user_lot[0:3] == reward_32first:
        sum_money += 4000
    if user_lot[3:6] == reward_31last:
        sum_money += 4000
    if user_lot[3:6] == reward_32last:
        sum_money += 4000
    if user_lot == reward_first:
        sum_money += 6000000

    nearby_1reward = int(reward_first) + 1
    nearby_2reward = int(reward_first) - 1
    if nearby_1reward > 999999:
        nearby_1reward = 0
    elif nearby_2reward < 0:
        nearby_2reward = 999999

    if user_lot == str(nearby_1reward).zfill(6):
        sum_money += 100000
    if user_lot == str(nearby_2reward).zfill(6):
        sum_money += 100000

    print(sum_money)
main()
