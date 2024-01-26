# lib/cli.py

from helpers import (
    exit_program,
    create_owner,
    update_owner,
    delete_owner,
    list_owners,
    find_owner_by_id,
    create_shoe,
    update_shoe,
    delete_shoe,
    list_shoes,
    list_shoes_by_owner_id,
    create_clear_database,
    seed_database
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "e" or "E":
            exit_program()
        elif choice == "c" or "C":
            create_owner()
        elif choice == "2":
            update_owner()
        elif choice == "3":
            delete_owner()
        elif choice == "4":
            list_owners()
        elif choice == "5":
            find_owner_by_id()
        elif choice == "6":
            create_shoe()
        elif choice == "7":
            update_shoe()
        elif choice == "8":
            delete_shoe()
        elif choice == "9":
            list_shoes()
        elif choice == "10":
            list_shoes_by_owner_id() 
        elif choice == "00":
            create_clear_database()
        elif choice == "s" or "S":
            seed_database()
        else:
            print("Invalid choice")


def menu():
    print('----------------------')
    print("Current owners")
    print("")
    list_owners()
    print("")
    print('----------------------')
    print("""
        Type a symbol below to perfrom its action
          
        #   Select that owner
        c   Create new owner 
        e   Exit program 
    """)



 
    # print("")
    # print("")
    # print("Please select an option:")
    # print("")
    # print("0. Exit the program")
    # print("1. Create owner")
    # print("2. Update owner")
    # print("3. Delete owner")
    # print("4. List owners")
    # print("5. Find owner by id")
    # print("6. Create shoe")
    # print("7. Update shoe")
    # print("8. Delete shoe")
    # print("9. List shoes")
    # print("10. List shoes by owner id")
    # print("11. Create/clear database")
    # print("12. Seed database")


if __name__ == "__main__":
    main()
