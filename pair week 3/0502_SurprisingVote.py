"""SurprisingVote"""
def main(total_score, most_score):
    """print ans"""
    score_left = total_score - most_score*2
    if total_score - most_score*2 < 0:
        score_left = 0
    if most_score - score_left > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))
