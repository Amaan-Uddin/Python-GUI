
from tkinter import *
import sqlite3

root = Tk()

database = sqlite3.connect("User_Details.db")
database_cursor = database.cursor()

database_cursor.execute("SHOW Details")

database.commit()
database.close()

root.mainloop()