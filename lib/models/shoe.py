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
            INSERT INTO shoes (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()

    def update(self):
        sql = """
            UPDATE shoes
            SET brand = ?, size = ?, type = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.brand, self.size, self.type, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM shoes
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None


    @classmethod
    def create(cls, brand, size, type):
        shoe = cls(brand, size, type)
        shoe.save()
        return shoe

    @classmethod
    def instance_from_db(cls, row):
        shoe = cls.all.get(row[0])
        if shoe:
            shoe.brand = row[1]
            shoe.size = row[2]
            shoe.type = row[3]
        else:
            shoe = cls(row[1], row[2], row[3])
            shoe.id = row[0]
            cls.all[shoe.id] = shoe
        return shoe
        

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM shoes
        """
        rows = CURSOR.execute(sql).fetchall()

        return[cls.instance_from_db(row) for row in rows]