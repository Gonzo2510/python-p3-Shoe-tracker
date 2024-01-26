import sqlite3

CONN = sqlite3.connect('shoe_tracker.db')
CURSOR = CONN.cursor()
