"""Turnstile"""
def main():
    """get value print ans"""
    have_coin = False
    can_pass = 0
    while True:
        user_act = input()
        if user_act == "END":
            break
        if user_act == "P" and have_coin:
            can_pass += 1
            have_coin = False
        if user_act == "C":
            have_coin = True
    print(can_pass)
main()
