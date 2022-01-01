# Random password generator Algorithm

from tkinter import * 
from random import *    
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk , Image   # We need this for our image insertion in our redo button



root = Tk()
root.title("Random Password Generator")
root.iconbitmap("visual_studio_code_icon_191771.ico")
root.geometry("1040x440")
root.config(bg = "slategrey")


database = sqlite3.connect("User_Details.db")
database_cursor = database.cursor()

item_no = 0
lower_case_characters = "abcdefghijklmnopqrstuvwxyz"
upper_case_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
symbols = "@#$&_%"

similar_char_1 =  ["a" , "A" , "@" , "4"]
similar_char_2 =  ["b" , "B" , "6" , "8"]
similar_char_3 =  ["c" , "C" , "e"]
similar_char_4 =  ["d" , "D"]
similar_char_5 =  ["e" , "E" , "c"]
similar_char_6 =  ["f" , "F" , "p" , "P"]
similar_char_7 =  ["g" , "G"]
similar_char_8 =  ["h" , "H" , "#"]
similar_char_9 =  ["i" , "I" , "1" , "l" , "L" , "j"]
similar_char_10 = ["j" , "J" , "7" , "i"]
similar_char_11 = ["k" , "K" , "R"]
similar_char_12 = ["l" , "L" , "i" , "1" , "I"]
similar_char_13 = ["m" , "M" , "N" , "n"]
similar_char_14 = ["n" , "N" , "M" , "m"]
similar_char_15 = ["o" , "O" , "0" , "Q"]
similar_char_16 = ["p" , "P" , "f" , "F"]
similar_char_17 = ["q" , "Q" , "9"]
similar_char_18 = ["r" , "R" , "K"]
similar_char_19 = ["s" , "S" , "$" , "5"]
similar_char_20 = ["t" , "T" , "I" , "1" , "f"]
similar_char_21 = ["u" , "U" , "v" , "V"]
similar_char_22 = ["v" , "V" , "u" , "U"]
similar_char_23 = ["w" , "W" , "V" , "v"]
similar_char_24 = ["x" , "X" , "Y"]
similar_char_25 = ["y" , "Y" , "X"]
similar_char_26 = ["z" , "Z" , "2"]

similar_char_lst = [
    similar_char_1   ,
    similar_char_2   , 
    similar_char_3   ,
    similar_char_4   , 
    similar_char_5   ,
    similar_char_6   , 
    similar_char_7   ,
    similar_char_8   ,
    similar_char_9   ,
    similar_char_10  ,
    similar_char_11  ,
    similar_char_12  ,
    similar_char_13  ,
    similar_char_14  ,
    similar_char_15  ,
    similar_char_16  ,
    similar_char_17  ,
    similar_char_18  ,
    similar_char_19  ,
    similar_char_20  ,
    similar_char_21  ,
    similar_char_22  ,
    similar_char_23  ,
    similar_char_24  ,
    similar_char_25  ,
    similar_char_26
]



# Let's open up an image:
my_image = ImageTk.PhotoImage(Image.open("visual_studio_code_icon_191771.ico"))   # now all we gotta do is specify this label in our "image" parameter and it will display the following image.
# We just created an image variable

# Create a function to defocus a widget:
def defocus_widget(event):
    event.widget.master.focus_set()

def pass_len_check(event):

    if lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True":
        if length_var.get() >= 10:
            length_var.set(10)

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True":
        if length_var.get() >= 6:
            length_var.set(6)

def func_setting(event):
    if setting_var.get() == "True":
        message = messagebox.askyesnocancel(title = "Confirm Changes" , message = "Are You Sure You Want To Save These Settings?")
        if message == True:
            print("yes")
            settings_save(event = None)
            setting_var.set("False")
        elif message == False:
            print("No")
            setting_var.set("False")
        else:
            setting_var.set("False")
            pass
    else:
        setting_var.set("False")


def insert_val(lower , upper , digit , symbl , rep , length):

    database = sqlite3.connect("User_Details.db")
    database_cursor = database.cursor()

    database_cursor.execute(""" INSERT INTO Details VALUES (:islower , :isupper , :isdigit , :issymbol , :no_repeat , :length)""" , 
                    {
                        "islower" : lower , 
                        "isupper" : upper , 
                        "isdigit" : digit , 
                        "issymbol" : symbl ,
                        "no_repeat" : rep ,
                        "length" : length ,
                    }

        )

    database.commit()
    database.close


def generate():

    user_new_password = ""

    if repeat_var.get() == "False":

        if lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True":
            
            option = lower_case_characters + upper_case_characters + digits + symbols
            gen_normal_pass(user_new_password , option)

            # This is one way of approaching the problem, another would be through the use of join() function...

            'user_new_password = "".join(choice(lower_case_characters+upper_case_characters+digits+symbols) for iteration in range(length_var.get()))'

            # This line of code will join the randomly selected word from our contcatinated string, 
            # attach it to our empty string and will repeat the process *length_var.get()* number of times

        elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False":
            
            option = lower_case_characters+upper_case_characters+digits
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True":

            option = lower_case_characters+upper_case_characters+symbols
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False":
            
            option = lower_case_characters+upper_case_characters
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True":

            option = lower_case_characters+digits+symbols
            gen_normal_pass(user_new_password , option)


        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False":

            option = lower_case_characters+digits
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True":

            option = lower_case_characters+symbols
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False":

            option = lower_case_characters
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True":

            option = upper_case_characters+digits+symbols
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False":

            option = upper_case_characters+digits
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True":

            option = upper_case_characters+symbols
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False":

            option = upper_case_characters
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True":

            option = digits+symbols
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False":

            option = digits
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True":

            option = symbols
            gen_normal_pass(user_new_password , option)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False":
            pass

    else:

        if lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True":

            user_new_password = "".join(choice(lower_case_characters+upper_case_characters+digits+symbols) for iteration in range(length_var.get()))

            user_options = lower_case_characters+upper_case_characters+digits+symbols

            unique_password(user_new_password , user_options)


        elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True":

            user_new_password = "".join(choice(lower_case_characters+upper_case_characters+digits) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters+upper_case_characters+digits

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(lower_case_characters+upper_case_characters+symbols) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters+upper_case_characters+symbols

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(lower_case_characters+upper_case_characters) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters+upper_case_characters

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(lower_case_characters+digits+symbols) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters+digits+symbols

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(lower_case_characters+digits) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters+digits

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(lower_case_characters+symbols) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters+symbols

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(lower_case_characters) for iteration in range(length_var.get()))
            
            user_options = lower_case_characters

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(upper_case_characters+digits+symbols) for iteration in range(length_var.get()))
            
            user_options = upper_case_characters+digits+symbols

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(upper_case_characters+digits) for iteration in range(length_var.get()))
            
            user_options = upper_case_characters+digits

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(upper_case_characters+symbols) for iteration in range(length_var.get()))
            
            user_options = upper_case_characters+symbols

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(upper_case_characters) for iteration in range(length_var.get()))
            
            user_options = upper_case_characters

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            user_new_password = "".join(choice(digits+symbols) for iteration in range(length_var.get()))
            
            user_options = digits+symbols

            unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True":

            if length_var.get() >= 10:
                length_var.set(10)
                user_new_password = "".join(choice(digits) for iteration in range(length_var.get()))
        
                user_options = digits

                unique_password(user_new_password , user_options)

            else:
                user_new_password = "".join(choice(digits) for iteration in range(length_var.get()))
        
                user_options = digits

                unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True":
            
            if length_var.get() >= 6:
                length_var.set(6)
                user_new_password = "".join(choice(symbols) for iteration in range(length_var.get()))
        
                user_options = symbols

                unique_password(user_new_password , user_options)

            else:
                user_new_password = "".join(choice(symbols) for iteration in range(length_var.get()))
        
                user_options = symbols

                unique_password(user_new_password , user_options)

        elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True":
            pass

def settings_save(event):

    database = sqlite3.connect("User_Details.db")
    database_cursor = database.cursor()


    if lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "True" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "True" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "True" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "True" and repeat_var.get() == "False" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "True":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "True" and setting_var.get() == "False":
        insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get() , length = length_var.get())

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "True":
        #insert_val(lower = lower_var.get() , upper = upper_var.get() , digit = number_var.get() , symbl = symbol_var.get() , rep = repeat_var.get())
        message = messagebox.showerror(title = "Selection Error" , message = "Please Select A Option Before Saving Your Setting.")
        if message == "ok":
            print("aight")
        else:
            print("tf?")

    elif lower_var.get() == "False" and upper_var.get() == "False" and number_var.get() == "False" and symbol_var.get() == "False" and repeat_var.get() == "False" and setting_var.get() == "False":
        pass


    database.commit()
    database.close()

def gen_normal_pass(password , options):

    for iteration in range(length_var.get()):
            password += choice(options)
            
            new_password_entry.config(state = ACTIVE)
            new_password_entry.delete(0 , END)
            new_password_entry.insert(0 , password)
            new_password_entry.config(foreground = "black" , state = "readonly")
            
            

def remove_astrixe(password , new_option):

    # This Function Will Replace The Astrixe With A Unique Character

    split_pass = password.split(" ")
    print(split_pass)
    for i in split_pass:
        lst = list(i)
        for j in lst:
            if j == "*":
                item = choice(new_option)
                lst_index = lst.index(j)
                lst.remove(j)
                lst.insert(lst_index , item)
                #i[j] = item
            else:
                pass

    # Now Once We Are Done With Replacing Our Astrixe We Can Then Move On Towards Converting Our List To A String
    
    new_pass = ""
    for item in range(len(lst)):
        new_pass += lst[item]

    return new_pass


def unique_password(password , option):

    tempo_lst = password.split(" ")  # We need to split our single string so we don't get an IndexError
    #duplicate_item_lst = []      <- remove for test runs
    new_pass = ""
    print(tempo_lst)

    # Remember 'i' and 'j' are just loop variables
    for i in tempo_lst:
        for j in range(len(i)):
            if i[j] in new_pass and i.count(i[j]) > 1:
                new_pass += "*"    # Place an astrixe where the duplicate item is 
                
            else:
                new_pass += i[j]

        else:

            if "*" in new_pass:
                new = remove_astrixe(new_pass , option)
                unique_password(new , option)
            else:
                print(new_pass)
                non_similer_char(new_pass , option)

def non_similer_char(password , non_similer_option):
    global item_no

    temp_list = password.split(" ")
    non_similer_pass = ""

    print(temp_list)

    lst = list(temp_list[0])

    for i in similar_char_lst:
        #print(f"i = {i}")        <- remove for test runs
        for j in i:
            #print(f"j = {j}")    <- remove for test runs
            for k in lst:
                #print(k)         <- remove for test runs
                if k == j and item_no == 1:
                    index = lst.index(k)
                    lst.remove(k)
                    lst.insert(index , "*")
                else:
                    if k == j and item_no != 1:
                        item_no += 1
                        break
        item_no = 0
    else:
        for item in range(len(lst)):
            non_similer_pass += lst[item]

        if "*" in lst:
            pass_1 = remove_astrixe(non_similer_pass , non_similer_option)
            unique_password(pass_1 , non_similer_option)

        else:
            print(non_similer_pass)
            new_password_entry.config(state = ACTIVE)
            new_password_entry.delete(0 , END)
            new_password_entry.insert(0 , non_similer_pass)
            new_password_entry.config(foreground = "black" , state = "readonly")

    # So first off this function is executed when there is no comman character or when no character is repeated
    # once we recieve our password which does not contain same characters we form a list of string using the split() function on our password string
    # then we create define/create an empty string(non_similer_pass)
    # create a list of characters from our list of string, and then iterate through our list(list of similar characters)
    # after that create another for-loop which would iterate through the list of items(characters which resemble each other or look similer) 
    # once we are done with that let's add another for-loop but this time the loop variable would iterate through our list of characters 
    # and check whether or not similer characters exist in that list.
    # if they do then it'll remove those characters and add a "*"
    # once the main/first for-loop end the loop-else will be executed where our non_similer_pass will recive all the characters from our list of characters.
    # after that we'll have 2 conditional statements , "if" will execute if our password contains similer characters and it'll go into a recursion
    # on the other hand the "else" statement will be executed if our password does not contain any similer characters or characters that resemble each other. 

def copy(event):
    copy_text = event.widget.get()
    root.clipboard_clear()
    root.clipboard_append(copy_text)
    return "break"

def copy_button(event):
    if new_password_entry.get() != "Your New Password":
        copy_text = new_password_entry.get()
        root.clipboard_clear()
        root.clipboard_append(copy_text)
    return "break"

# Create tkinter variables:
length_var = IntVar()
length_var.set(4)

upper_var = StringVar()
upper_var.set("False")

lower_var = StringVar()
lower_var.set("False")

number_var = StringVar()
number_var.set("False")

symbol_var = StringVar()
symbol_var.set("False")

repeat_var = StringVar()
repeat_var.set("False")

setting_var = StringVar()
setting_var.set("False")

password_var = StringVar()
password_var.set("Your New Password")


# Create a style for our ttk widgets

text_style = ttk.Style()
text_style.configure("TCheckbutton" , font = ("Helvetica" , 12 , "italic" , "bold") , background = "slategrey" , foreground = "snow")
text_style.configure("TButton" , font = ("Helvetica" , 11) , background = "slategrey")


bg_style = ttk.Style()
bg_style.configure("TFrame" , bg = "blue")

# TCheckbutton for Checkbutton , TButton for Button etc...


# Create option list:
length_options = [4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16]

# Labels:

project_label = ttk.Label(root , text = "Password-Generator" , font = ("Helvetica" , 15) , anchor = E , background = "lightslategrey" , foreground = "lightcyan")
project_label.grid(row = 0 , column = 0 , columnspan = 4 , sticky = W + E)

password_length = ttk.Label(root , text = "Password Length :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
password_length.grid(row = 1 , column = 0 , pady = (24 , 11) , padx = (0 , 5) , sticky = NSEW)

lower_case = ttk.Label(root , text = "Include Lower-Case :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
lower_case.grid(row = 2 , column = 0 , pady = (0 , 10) , padx = (0, 5), sticky = NSEW)

upper_case = ttk.Label(root , text = "Include Upper-Case :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
upper_case.grid(row = 3 , column = 0 , pady = (0 , 10) , padx = (0 , 5) , sticky = NSEW)

numbers = ttk.Label(root , text = "Include Numbers :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
numbers.grid(row = 4 , column = 0 , pady = (0 , 10) , padx = (0 , 5) , sticky = NSEW)

symbols_label = ttk.Label(root , text = "Include Symbols :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
symbols_label.grid(row = 5 , column = 0 , pady = (0 , 10) , padx = (0 , 5) , sticky = NSEW)

repeat = ttk.Label(root , text = "No-Repetitive Characters :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
repeat.grid(row = 6 , column = 0 , pady = (0 , 10) , padx = (0 , 5) , sticky = NSEW)

settings = ttk.Label(root , text = "Save My Settings :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
settings.grid(row = 7 , column = 0 , pady = (0 , 10) , padx = (0 , 5) , sticky = NSEW)

new_password = ttk.Label(root , text = "Your Password :" , anchor = E , font = ("Helvetica" , 12) , background = "slategrey" , foreground = "snow")
new_password.grid(row = 9 , column = 0 , pady = (14 , 25) , padx = (0 , 5) , sticky = NSEW)


# Buttons/Checkbuttons/boxes/Entry:

password_length_box = ttk.Combobox(root , textvariable = length_var , values = length_options , width = 35 , height = 6 , background = "slategrey")
password_length_box.bind("<<ComboboxSelected>>" , pass_len_check)
password_length_box.bind("<FocusIn>" , defocus_widget)
password_length_box.grid(row = 1 , column = 1 , pady = (25 , 10) , sticky = W )

lower_case_button = ttk.Checkbutton(root , text = "(e.g. abcdefg)" , variable = lower_var , onvalue = "True" , offvalue = "False" , style = "TCheckbutton")
lower_case_button.bind("<FocusIn>" , defocus_widget)
lower_case_button.grid(row = 2 , column = 1 , pady = (0 , 10) , sticky = W)

upper_case_button = ttk.Checkbutton(root , text = "(e.g. ABCDEFG)" , variable = upper_var , onvalue = "True" , offvalue = "False" , style = "TCheckbutton")
upper_case_button.bind("<FocusIn>" , defocus_widget)
upper_case_button.grid(row = 3 , column = 1 , pady = (0 , 10) , sticky = W)

numbers_button = ttk.Checkbutton(root , text = "(e.g. 1234567890 )" , variable = number_var , onvalue = "True" , offvalue = "False" , style = "TCheckbutton")
numbers_button.bind("<Button-1>" , pass_len_check)
numbers_button.bind("<FocusIn>" , defocus_widget)
numbers_button.grid(row = 4 , column = 1 , pady = (0 , 10) , sticky = W)

symbols_button = ttk.Checkbutton(root , text = "(e.g. @ , # , $ , % , &)" , variable = symbol_var , onvalue = "True" , offvalue = "False" , style = "TCheckbutton")
symbols_button.bind("<Button-1>" , pass_len_check)
symbols_button.bind("<FocusIn>" , defocus_widget)
symbols_button.grid(row = 5 , column = 1 , pady = (0 , 10) , sticky = W)

repeat_button = ttk.Checkbutton(root , text = "( Do Not Repeat The Same Character Twice )" , variable = repeat_var , onvalue = "True" , offvalue = "False" , style = "TCheckbutton")
repeat_button.bind("<Button-1>" , pass_len_check)
repeat_button.bind("<FocusIn>" , defocus_widget)
repeat_button.grid(row = 6 , column = 1 , pady = (0 , 10) , sticky = W)

setting_save_button = ttk.Checkbutton(root , text = "( Save These Settings For Later Use Or Updating ) " , variable = setting_var , onvalue = "True" , offvalue = "False" , style = "TCheckbutton" , command = lambda:func_setting("Button-1"))
setting_save_button.bind("<FocusIn>" , defocus_widget)
setting_save_button.grid(row = 7 , column = 1 , pady = (0 , 10) , sticky = W)

generate_password = ttk.Button(root , text = "Generate Password" , command = generate , style = "TButton" , width = 18)
generate_password.bind("<FocusIn>" , defocus_widget)
generate_password.grid(row = 8 , column = 1 , pady = (10 , 10) , ipadx =  10 , sticky = W , ipady = 5)

new_password_entry = ttk.Entry(root ,  textvariable = password_var , width = 50  , foreground = "grey" , font = ("Helvetica" , 11) , background = "slategrey" , state = DISABLED)
new_password_entry.bind("<FocusIn>" , defocus_widget)
new_password_entry.bind("<Button-3>" , copy)
new_password_entry.grid(row = 9 , column = 1 , pady = (10 , 25) , ipady = 3 , sticky = W) # Use ipady to increase the internal padding of entry boxes

copy_ = ttk.Button(root , text = "copy", command = lambda:copy_button("<Button-1>"))        # Insert a redo image once the internet problem is fixed
copy_.bind("<FocusIn>" , defocus_widget)
copy_.grid(row = 9 , column = 2 , sticky = W  , pady = (10 ,25) , ipady = 2 , padx = (10 , 0) )

# Create an instruction frame:

outter_frame = Frame(root , bg = "blue")
outter_frame.grid(row = 1  , column = 2 , rowspan = 8 , sticky = NW , padx = (10 , 10) , pady = (55 , 10))

inner_frame = Frame(outter_frame , bg = "skyblue")
inner_frame.grid(row = 0 , column = 0 , padx = 1 , pady = 1 , ipady = 7)

text_list = [
    "                                     Instructions" ,
    "1. Generate A Password Of Your Choice" , 
    "2. Generate A Passcode For Your Mobile Device" , 
    "3. Save Your Settings For Future Reference" ,
    "4. Select 'No-Repeititive Chracters' For A Strong Password"
]

for num , text  in  enumerate(text_list):
    info = Label(inner_frame , text = text , background = "skyblue" , font = ("Arial" , 10 , "bold") , anchor = W , fg = "snow")
    info.grid(row = num , column = 0 , sticky = W , padx = 10 , pady = 6)


database.commit()
database.close()

'''def re_size(event):     <- function to resize widgets when maximized
    if root.state() == "zoomed":
        password_length.configure(font = ("Helvetica" , 20))
        password_length_box.configure(width = 45  , font = ("Helvetica" , 10))
        password_length_box.grid_configure(ipady = 3)

    else:
        #root.state() == "normal":
        password_length.configure(font = ("Helvetica" , 12))
        password_length_box.configure(width = 35 )
        password_length_box.grid_configure(ipady = 0)'''

'root.bind("<Configure>" , re_size)'

root.grid_columnconfigure(0 , weight = 1)
root.grid_columnconfigure(3 , weight = 1)

root.rowconfigure(1 , weight = 1)
root.rowconfigure(2 , weight = 1)
root.rowconfigure(3 , weight = 1)
root.rowconfigure(4 , weight = 1)
root.rowconfigure(5 , weight = 1)
root.rowconfigure(6 , weight = 1)
root.rowconfigure(7 , weight = 1)
root.rowconfigure(8 , weight = 1)
root.rowconfigure(9 , weight = 1)



root.mainloop()
