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
    list_shoes_by_owner_id
)






def menu():
    print('----------------------')
    print("Current owners")
    print("")
    list_owners()
    print("")
    print('----------------------')
    print("""
        Type a symbol below to perfrom an action
          
        #   Select that owner
        C   Create new owner 
        E   Exit program
        CD  Clear database
        S   Seed database
    """)

    choice = input("> ").upper()

    if choice == "E":
        exit_program()
    elif choice == "C":
        create_owner()
    elif choice.isdigit() and 1 <= int(choice) <= len(list_owners()):
        owner_menu(choice)
    else:
        print("Invalid choice")


def owner_menu(choice):
    print('----------------------')
    print(f'Owner {find_owner_by_id()}')
    print("")

    print("")
    print('----------------------')
    print("""
        Type a symbol below to perfrom an action
          
        #   Select that owner
        C   Create new owner 
        E   Exit program
    """)


def main():
    while True:
        menu()

if __name__ == "__main__":
    main()
