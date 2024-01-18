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

    def __init__(self, brand, size, person_id, id=None):
        self.id = id
        self.brand = brand
        self.size = int(size)
        self.person_id = person_id

    def __repr__(self) -> str:
        return(
            f"Shoe {self.id}: {self.brand}, {self.size}, {self.person_id}"
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
            brand TEXT,
            size INTEGER,
            person_id INTEGER,
            FOREIGN KEY (person_id) REFERENCES persons(id))
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
            INSERT INTO shoes (
                brand,
                size,
                person_id)
            VALUES (?, ?, ? )
        """
        CURSOR.execute(sql, (self.brand, self.size, self.person_id))
        CONN.commit()

    def update(self):
        sql = """
            UPDATE shoes
            SET brand = ?, size = ?, person_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.brand, self.size, self.person_id, self.id))
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
    def create(cls, brand, size, person_id):
        shoe = cls(brand, size, person_id)
        shoe.save()
        return shoe

    @classmethod
    def instance_from_db(cls, row):
        shoe = cls.all.get(row[0])
        if shoe:
            shoe.brand = row[1]
            shoe.size = row[2]
            shoe.person_id = row[3]
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
    

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM shoes
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None