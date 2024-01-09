# lib/cli.py

from helpers import (
    exit_program,
    create_person,
    update_person,
    delete_person,
    list_persons,
    find_person_by_id,
    create_shoe,
    update_shoe,
    delete_shoe,
    list_shoes
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_person()
        elif choice == "2":
            update_person()
        elif choice == "3":
            delete_person()
        elif choice == "4":
            list_persons()
        elif choice == "5":
            find_person_by_id()
        elif choice == "6":
            create_shoe()
        elif choice == "7":
            update_shoe()
        elif choice == "8":
            delete_shoe()
        elif choice == "9":
            list_shoes()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create person")
    print("2. Update person")
    print("3. Delete person")
    print("4. List persons")
    print("5. Find person by id")
    print("6. Create shoe")
    print("7. Update shoe")
    print("8. Delete shoe")
    print("9. List shoes")



if __name__ == "__main__":
    main()
