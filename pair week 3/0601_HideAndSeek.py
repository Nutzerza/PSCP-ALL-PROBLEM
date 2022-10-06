"""HideAndSeek"""
def main(start, end, plus):
    """print ans"""
    for count in range(start, end, plus):
        print(count)
main(int(input()), int(input()), int(input()))
