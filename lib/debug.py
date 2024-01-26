#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.owner import Owner
from models.shoe import Shoe

def reset_database():
    Shoe.drop_table()
    Owner.drop_table()
    Owner.create_table()
    Shoe.create_table()
    print("Database cleared")

def seed_database():
    Owner.create("Jacob")
    Owner.create("Isabel")
    Owner.create("Aaron")
    Owner.create("Joe")

    Shoe.create("Puma", 8, 2)
    Shoe.create("Nike", 13, 1)
    Shoe.create("Reebok", 12, 3)
    Shoe.create("Adidas", 11, 4)
    Shoe.create("Converse", 8, 2)
    Shoe.create("Under Armour", 8, 2)
    Shoe.create("Vans", 8, 2)
    Shoe.create("Jordan", 8, 2)
    Shoe.create("Nike", 8, 2)

    print("Database seeded")

breakpoint()
