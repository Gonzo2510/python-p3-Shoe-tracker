from models.__init__ import CURSOR, CONN


class Shoe:
    all = {}

    shoe_brands = [
    "Adidas",
    "Converse",
    "Jordan",
    "New Balance",
    "Nike",
    "Puma",
    "Reebok",
    "Salomon",
    "Under Armour",
    "Vans"
]

    def __init__(self, brand, size, type, id=None):
        self.id = id
        self.brand = brand
        self.size = size
        self.type = type

    def __repr__(self) -> str:
        return(
            f"Shoe {self.id}: {self.brand}, {self.type}"
        )
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if brand.title() in Shoe.shoe_brands:
            self._brand = brand
        else:
            raise ValueError(
                f"Name must be one of the following: {Shoe.shoe_brands}"
            )
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS shoes (
            id INTEGER PRIMARY KEY,
            brand TEXT
            size INTEGER
            type TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS shoes;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO departments (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name))
        CONN.commit()