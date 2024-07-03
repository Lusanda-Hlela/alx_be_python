# Shopping List Manager

# Use Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Exit")

def main():
  shopping_list = []
  while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item: ")
        shopping_list.append(item)
        pass
    elif choice == "2":
        print(shopping_list)
        pass
    elif choice == "3":
        item = input("Enter the item to remove: ")
        shopping_list.remove(item)
        pass
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
