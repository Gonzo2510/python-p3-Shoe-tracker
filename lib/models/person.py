from models.__init__ import CURSOR, CONN
from models.shoe import Shoe

class Person:

    all ={}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f"<Person {self.id}: {self.name}>"