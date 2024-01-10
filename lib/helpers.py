from models.person import Person
from models.shoe import Shoe

# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


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
    pass


def create_shoe():
    pass

def update_shoe():
    pass

def delete_shoe():
    pass

def list_shoes():
    pass
