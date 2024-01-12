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
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Person instances """
        sql = """
            CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Person instances """
        sql = """
            DROP TABLE IF EXISTS persons;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Person instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO persons (
                name
                id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        # type(self).all[self.id] = self


    @classmethod
    def create(cls, name):
        person = cls(name)
        person.save()
        return person
    
    def update(self):
        sql = """
            UPDATE persons
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM persons
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        person = cls.all.get(row[0])
        if person:
            person.name = row[1]
        else:
            person = cls(row[1])
            person.id = row[0]
            cls.all[person.id] = person
        return person

    def get_all():
        pass

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM persons
        """

        rows = CURSOR.execute(sql).fetchall()

        return[cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM persons
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None