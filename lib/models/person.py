from models.__init__ import CURSOR, CONN
from models.shoe import Shoe

class Person:

    all ={}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f"<Person {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )