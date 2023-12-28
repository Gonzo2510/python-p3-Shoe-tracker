from models.__init__ import CURSOR, CONN


class Shoe:
    all ={}

    def __init__(self, brand, size, type, id=None):
        self.id = id
        self.brand = brand
        self.size = size
        self.type = type

    def __repr__(self) -> str:
        return(
            f"Shoe {self.id}: {self.brand}, {self.type}"
        )