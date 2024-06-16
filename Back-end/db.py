import sqlite3

conn = sqlite3.connect('pic.sqlite3', check_same_thread = False )

cursor = conn.cursor()