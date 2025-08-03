# main.py

import sys

def run_division_calculator():
    from robust_division_calculator import safe_divide

    if len(sys.argv) != 4:
        print("Usage for division: python main.py division <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[2]
    denominator = sys.argv[3]
    result = safe_divide(numerator, denominator)
    print(result)


def run_library_management():
    from library_management import Book, Library

    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py division <numerator> <denominator>")
        print("  python main.py library")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "division":
        run_division_calculator()
    elif mode == "library":
        run_library_management()
    else:
        print("Unknown mode. Use 'division' or 'library'.")

if __name__ == "__main__":
    main()
