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
    # list_shoes_by_owner_id
)


def menu():
    owners = list_owners()
    shoes = list_shoes()
    print('----------------------')
    print("Current Owners: ")
    print("")
    for i, owner in enumerate(owners, start=1):
        print(f'{i}. {owner.name}')
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
        id_ = owners[int(choice)-1].id
        owner_menu(id_)
    else:
        print("Invalid choice")


def owner_menu(id):
    while True:
        owner = find_owner_by_id(id)
        shoes = owner.shoes()
        print('----------------------')
        print(f'{owner.name}\'s shoes:')
        print("")
        if shoes:
            for i, shoe in enumerate(shoes, start=1):
                print(i, shoe.brand, shoe.size)
        else:
            print('No owned shoes...')
        print('----------------------')
        print("""
        Type a symbol below to perform an action
        
        U   Update owner's name
        D   Delete owner
        C   Create new shoe
        US  Update a shoe
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
        elif choice == "US":
            update_shoe(owner)
        elif choice == "DS":
            delete_shoe(owner)
        elif choice == "B":
            break
        else:
            print("Invalid choice")


def main():
    while True:
        menu()

if __name__ == "__main__":
    main()