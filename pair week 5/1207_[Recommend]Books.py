"""[Recommend] Books""" #2 Timeout
def main(book, page, num_x, num_y):
    """print ans"""
    day = 0
    page_read = page
    while book > 0:
        can_read = page * (num_x + day) / (num_y + day)
        if can_read > int(can_read):
            can_read = int(can_read)+1

        if can_read >= page:
            day += book
            break

        page_read -= can_read

        if page_read <= 0:
            page_read = page
            book -= 1
        day += 1

    print(day)
main(int(input()), int(input()), int(input()), int(input()))
