# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
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
            helper_1()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            pass
        elif choice == "11":
            pass
        elif choice == "12":
            pass
        elif choice == "13":
            pass
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
