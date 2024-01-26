from models.owner import Owner
from models.shoe import Shoe

# lib/helpers.py


def exit_program():
    print("Goodbye!")
    exit()

def create_owner():
    name = input("Enter owner name: ")
    try:
        owner = Owner.create(name)
        print(f'Success: {owner}')
    except Exception as exc:
        print("Error creating owner: ", exc)
        
def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner) 

def update_owner():
    print("")
    list_owners()
    print("")
    id_ = input("Enter the owner's id: ")
    if owner := Owner.find_by_id(id_):
        try:
            name = input("Enter owner's new name: ")
            owner.name = name

            owner.update()
            print(f'Success: {owner}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_owner():
    print("")
    list_owners()
    print("")
    id_ = input("Enter the owner's id: ")
    if owner := Owner.find_by_id(id_):
        owner.delete()
        print(f'Owner {id_} deleted')
    else:
        print(f'Owner {id_} not found')

def find_owner_by_id():
    id_ = input("Enter the owner's id: ")
    owner = Owner.find_by_id(id_)
    print(owner) if owner else print(f'Owner {id_} not found')

def create_shoe():
    print("")
    print(Shoe.shoe_brands)
    brand = input("Enter the shoe brand from above: ")
    size = input("Enter the shoe size: ")
    print("")
    list_owners()
    print("")
    owner_id = input("Enter the shoe's owner id: ")
    try:
        size = int(size)
        shoe = Shoe.create(brand, size, owner_id)
        print(f'Success: {shoe}')
    except Exception as exc:
        print("Error creating shoe: ", exc)

def list_shoes():
    shoes = Shoe.get_all()
    for shoe in shoes:
        print(shoe) 

def update_shoe():
    print("")
    list_shoes()
    print("")
    id_ = input("Enter the shoe's id: ")
    if shoe := Shoe.find_by_id(id_):
        try:
            brand = input("Enter the shoe brand: ")
            shoe.brand = brand
            size = input("Enter the shoe size: ")
            shoe.size = int(size)
            owner_id = input("Enter the shoe's owner id: ")
            shoe.type = owner_id

            shoe.update()
            print(f'Success: {shoe}')
        except Exception as exc:
            print("Error updating shoe: ", exc)

def delete_shoe():
    print("")
    list_shoes()
    print("")
    id_ = input("Enter the shoe's id: ")
    if shoe := Shoe.find_by_id(id_):
        shoe.delete()
        print(f'Shoe {id_} deleted')
    else:
        print(f'Shoe {id_} not found')

def list_shoes_by_owner_id():
    owner_id = input("Enter the owner's id: ")
    owner = Owner.find_by_id(owner_id)
    if owner:
        owner_shoes = owner.shoes()
        for shoe in owner_shoes:
            print(shoe)