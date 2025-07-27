# Global shopping list
shopping_list = []

# Function to display menu
def display_menu():
    """Displays the shopping list menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main program loop
def main():
    while True:
        display_menu()  # Call menu at the beginning of each loop

        choice_input = input("Enter your choice (1-4): ")

        if not choice_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice_input)

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the list.")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")

        elif choice == 3:
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run main function
if __name__ == "__main__":
    main()
