"""[Recommend] Squid Game 3 - Tug-of-War"""
def main():
    """get value print ans"""
    power_team_a = 0
    power_team_b = 0

    for counter in range(20):
        power_player = int(input())
        if counter < 10:
            power_team_a += power_player
        else:
            power_team_b += power_player

    if power_team_a == power_team_b:
        print("AB")
    elif power_team_a > power_team_b:
        print("B")
    elif power_team_a < power_team_b:
        print("A")
main()
