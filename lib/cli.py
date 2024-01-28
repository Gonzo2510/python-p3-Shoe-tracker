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
    print("Current Owners: ")
    print("")
    list_owners()
    print("")
    print('----------------------')
    print("""
        Type a symbol below to perform an action
          
        #   Select that owner
        C   Create new owner 
        E   Exit program
    """)

    choice = input("> ").upper()
 
    if choice == "E":
        exit_program()
    elif choice == "C":
        create_owner()
    elif choice.isdigit():
        owner_menu(choice)
    else:
        print("Invalid choice")


def owner_menu(id):
    while True:
        owner = find_owner_by_id(id)
        print('----------------------')
        print(f'{owner.name}\'s shoes:')
        print("")
        print(list_shoes_by_owner_id(id))
        print('----------------------')
        print("""
        Type a symbol below to perform an action
        
        U   Update owner's name
        D   Delete owner
        C   Create new shoe
        DS  Delete a shoe
        B   Back to main menu
        E   Exit program
        """)

        choice = input("> ").upper()
    
        if choice == "E":
            exit_program()
        elif choice == "U":
            update_owner(id)
        elif choice == "D":
            delete_owner(id)
            break
        elif choice == "C":
            create_shoe(id)
        elif choice == "DS":
            delete_shoe()
        elif choice == "B":
            break
        else:
            print("Invalid choice")


def main():
    while True:
        menu()

if __name__ == "__main__":
    main()