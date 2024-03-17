checkouts = []

def check_out_book(book):
        if book in checkouts:
            return False
        else:
            checkouts.append(book)
            return True


def check_in_book(book):
        if book in checkouts:
            checkouts.remove(book)
            return True
        else:
            return False
