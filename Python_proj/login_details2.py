from tkinter import *
import sqlite3

root = Tk()

# let's create our data-base
data_base = sqlite3.connect("User_Details.db")

# Create a cursor for our data-base
data_base_cursor = data_base.cursor()

data_base.execute("ALTER TABLE Details ADD COLUMN '{cn}'  {ct}" . format(cn = "length" , ct = "text"))

# Commit all the chnages in our data-base
data_base.commit()

# Close our data-base
data_base.close()

root.mainloop()