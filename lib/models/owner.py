from models.__init__ import CURSOR, CONN

class Owner:

    all ={}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f"{self.id}: {self.name}"
    
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
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Owner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Owner instances """
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Owner instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO owners (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        # type(self).all[self.id] = self


    @classmethod
    def create(cls, name):
        owner = cls(name)
        owner.save()
        return owner
    
    def update(self):
        sql = """
            UPDATE owners
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM owners
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        owner = cls.all.get(row[0])
        if owner:
            owner.name = row[1]
        else:
            owner = cls(row[1])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner

    def get_all():
        pass

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM owners
        """
        
        try:
            rows = CURSOR.execute(sql).fetchall()
        except: 
            Owner.create_table()
            rows = CURSOR.execute(sql).fetchall()

        return[cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def shoes(self):
        from models.shoe import Shoe
        sql = """
            SELECT * FROM shoes
            WHERE owner_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
    
        rows = CURSOR.fetchall()
        return[
            Shoe.instance_from_db(row) for row in rows
        ]