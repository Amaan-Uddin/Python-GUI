# Create a data-base
from tkinter import *
import sqlite3

root = Tk()

# let's create our data-base
data_base = sqlite3.connect("User_Details.db")

# Create a cursor for our data-base
data_base_cursor = data_base.cursor()

data_base.execute('''CREATE TABLE Details(
        first_name text,
        last_name text,
        email text,
        password text)'''
)

# Commit all the chnages in our data-base
data_base.commit()

# Close our data-base
data_base.close()

root.mainloop()