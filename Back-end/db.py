import sqlite3

conn = sqlite3.connect('games.sqlite3', check_same_thread = False )

cursor = conn.cursor()