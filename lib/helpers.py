from models.person import Person
from models.shoe import Shoe

# lib/helpers.py


def exit_program():
    print("Goodbye!")
    exit()

def create_person():
    name = input("Enter person name: ")
    try:
        person = Person.create(name)
        print(f'Success: {person}')
    except Exception as exc:
        print("Error creating person: ", exc)
        
def update_person():
    id_ = input("Enter the person's id: ")
    if person := Person.find_by_id(id_):
        try:
            name = input("Enter person's new name: ")
            person.name = name
            new_id = input("Enter person's new id: ")
            person.id = new_id
            person.update()
            print(f'Success: {person}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_person():
    id_ = input("Enter the person's id: ")
    if person := Person.find_by_id(id_):
        person.delete()
        print(f'Person {id_} deleted')
    else:
        print(f'Person {id_} not found')

def list_persons():
    persons = Person.get_all()
    for person in persons:
        print(person) 

def find_person_by_id():
    id_ = input("Enter the person's id: ")
    person = Person.find_by_id(id_)
    print(person) if person else print(f'Person {id_} not found')

def create_shoe():
    brand = input("Enter the shoe brand: ")
    size = input("Enter the shoe size: ")
    type = input("Enter the shoe type: ")
    try:
        size = int(size)
        shoe = Shoe.create(brand, size, type)
        print(f'Success: {shoe}')
    except Exception as exc:
        print("Error creating shoe: ", exc)

def update_shoe():
    id_ = input("Enter the shoe's id: ")
    if shoe := Shoe.find_by_id(id_):
        try:
            brand = input("Enter the shoe brand: ")
            shoe.brand = brand
            size = input("Enter the shoe size: ")
            shoe.size = int(size)
            type = input("Enter the shoe type: ")
            shoe.type = type

            shoe.update()
            print(f'Success: {shoe}')
        except Exception as exc:
            print("Error updating shoe: ", exc)

def delete_shoe():
    id_ = input("Enter the shoe's id: ")
    if shoe := Shoe.find_by_id(id_):
        shoe.delete()
        print(f'Shoe {id_} deleted')
    else:
        print(f'Shoe {id_} not found')

def list_shoes():
    shoes = Shoe.get_all()
    for shoe in shoes:
        print(shoe) 


def create_clear_database():
    Shoe.drop_table()
    Person.drop_table()
    Person.create_table()
    Shoe.create_table()
    print("Database cleared")