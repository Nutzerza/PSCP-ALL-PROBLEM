"""Nearer"""
def main(alice, bob, ice_cream):
    """print ans"""
    alice_ice = abs(ice_cream - alice)
    bob_ice = abs(ice_cream - bob)
    if alice_ice > bob_ice:
        print("Bob", bob_ice)
    elif alice_ice < bob_ice:
        print("Alice", alice_ice)
    else:
        print("Sundaes", alice_ice)
main(int(input()), int(input()), int(input()))
