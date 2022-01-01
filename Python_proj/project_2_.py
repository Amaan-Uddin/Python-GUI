
from tkinter import * 
from tkinter import ttk
import sqlite3
from random import *



root = Tk()
root.title("Random PASS Generator")
root.iconbitmap("visual_studio_code_icon_191771.ico")
# origional 650x400
root.geometry("630x287")

database = sqlite3.connect("User_Details.db")
database_cursor = database.cursor()

emailvar = StringVar()
emailvar.set("example@email.com")

passvar = StringVar()

email_menu = StringVar()
email_menu.set("@gmail.com")

password_menu = StringVar()
password_menu.set("show")

options_1 = [
    "@gmail.com" , 
    "@yahoo.com" ,
    "@icloud.com" , 
    "clear"
]

options_2 = [
    "-show-" , 
    "-hide-" , 
    "clear"
]

invalid_option = [
    "*Invalid Email or Password : " , 
    "   .Please make sure that your email address is correct." , 
    "   .or make sure that the password given is correct." ,
    "   .Please attach the correct email ID."
]


def random_pass_generator():
    pass


def check_authentication(email,password):
    global email_entry
    global password_entry

    root.geometry("630x287")

    database = sqlite3.connect("User_Details.db")
    database_cursor = database.cursor()

    database_cursor.execute(""" SELECT * , oid FROM Details""")
    database_records = database_cursor.fetchall()

    for record in database_records:
        if email and password in record:
            print(email , password)
            random_pass_generator()
            exterior_frame_3 = Frame(root , width =  53 , height = 21 ,background = "blue")
            exterior_frame_3.grid(row = 8 , column = 1 , pady = (0 , 10) , sticky = W + E)

            info_frame_3 = Frame(exterior_frame_3 , width = 53 , height = 20 , background = "mediumspringgreen")
            info_frame_3.grid(row = 0 , column = 0 , sticky = NSEW , padx = 1 , pady = 1)

            Label(info_frame_3 , text = f"{email} {password}" , fg = "white" , font = ("Helvetica" , 10 , "italic") , bg = "mediumspringgreen" , anchor = CENTER).grid(row = 0 , column = 0 , padx = 10 , ipadx = 32)
            break
    else:
        root.geometry("630x316")
        exterior_frame_3 = Frame(root , width = 56 , height = 21 , background = "red")
        exterior_frame_3.grid(row = 8 , column = 1 , pady = (0, 10) , sticky = W+E)

        info_frame_3 = Frame(exterior_frame_3 , width = 55 , height = 20 , background = "pink")
        info_frame_3.grid(row = 0 , column = 0 , sticky = NSEW , padx = 1 , pady = 1) 

        Label(info_frame_3 , text = "Record not found...\n-Please try again- ", font = (None , 10) , fg = "red" , bg = "pink" , anchor = N).grid(row = 0 , column = 0 , padx = 10 , ipadx = 113 , sticky = W+E)



    database.commit()
    database.close()

    email_entry.delete(0 , END)
    password_entry.delete(0 , END)

def first_bit():
    global email_entry
    global password_entry
    global exterior_frame
    global exterior_frame_2
    global info_frame
    global info_frame_2
    global number
    global number_1
    global show_once
    global show_another

    number = 0
    number_1 = 0

    show_once = 0
    show_another = 0

    ''' we defined 2 variables show_once and show_another so that we don't  encounter a bug which would 
        stop the program from deleting the 2 exterior frames if they were present on the screen.
    '''

    def focus_next_window(event):
        event.widget.tk_focusNext().focus()
        return("break")

    # The method tk_focusNext() returns the NEXT widget in the keyboard traversel hieracrchy.
    # The method focuss() set's the focus to that widget
    # returning "break" is critical because it prevents the class binding from firing.
    # It is this class binding that inserts the tab character , which you don't want.

    def email_click(event):
        if email_entry.get() == "example@email.com":
            event.widget.delete(0 , END)
            email_entry.config(fg = "black")
        else:
            pass

    def pass_click(event):
        if email_entry.get() == "":
            email_entry.config(fg = "grey")
            email_entry.insert(0 , "example@email.com")


    def highlight_user_button(event):
        new_user_button.config(font = ("Helvetica", 11 , "bold" , "underline") , fg = "blue" , bg = "skyblue")
    def un_highlight_user_button(event):
        new_user_button.config(font = ("Helvetica", 11) , fg = "black" , bg = "gainsboro")

    def highlight_confirm_button(event):
        confirm_button.config(font = ("Helvetica", 11 , "bold" , "underline") , fg = "blue" , bg = "springgreen")
    def un_highlight_confirm_button(event):
        confirm_button.config(font = ("Helvetica", 11 ) , fg = "black" , bg = "gainsboro")


    def addresses(event):

        if email_menu.get() != "clear" and email_entry.get() != "example@email.com":
            email_entry.config(fg = "black")
            user_name = email_entry.get()
            user_address = email_menu.get()
            new_email = user_name + user_address
            for item in new_email.split("@"):
                new_email = item + email_menu.get()
                break
            email_entry.delete(0 , END)
            email_entry.insert(0 , new_email)
            

        else:
            email_entry.delete(0 , END)


    def show_pass(event):

        if password_menu.get() == "-show-":
            password_entry.config(show = "")
            password_menu.set("show")

        elif password_menu.get() == "-hide-":
            password_entry.config(show = "*")
            password_menu.set("hide")

        else:
            password_entry.delete(0 , END)

            
    def repeat():
        global exterior_frame
        global info_frame
        global number
 
        exterior_frame = Frame(root , width = 56 , height = 21 , background = "red")
        exterior_frame.grid(row = 6 , column = 1 , pady = (0, 20) , sticky = W+E)

        info_frame = Frame(exterior_frame , width = 55 , height = 20 , background = "pink")
        info_frame.grid(row = 0 , column = 0 , sticky = NSEW , padx = 1 , pady = 1)

        for num , text in enumerate(invalid_option): # Returns index and the value at that index
            info_label = Label(info_frame , text = text , font = (None , 10) , fg = 'red' , bg = "pink" , anchor = CENTER)
            info_label.grid(row = num ,  column = 1 , sticky = W , pady = (5 , 10) , padx = (10 , 24))
        number = 1
       

    def display_error():
        global exterior_frame_2
        global info_frame_2
        global number_1

        exterior_frame_2 = Frame(root , width = 56 , height = 21 , background = "red")
        exterior_frame_2.grid(row = 3 , column = 1 , pady = (0, 10) , sticky = W+E)

        info_frame_2 = Frame(exterior_frame_2 , width = 55 , height = 20 , background = "pink")
        info_frame_2.grid(row = 0 , column = 0 , sticky = NSEW , padx = 1 , pady = 1) 

        Label(info_frame_2 , text = "Please attach a valid email address.." , font = (None , 10) , fg = "red" , bg = "pink" , anchor = CENTER).grid(row = 0 , column = 0 , padx = 10 , ipadx = 62)
        number_1 = 1


    def deleting_frame(first , second):
        global exterior_frame
        global exterior_frame_2

        if first >= 1:
            exterior_frame.grid_forget()
        if second >= 1:
            exterior_frame_2.grid_forget()


    def second_confirm():
        global show_once
        global show_another
        global number_1
        global number

        if "@gmail.com" in email_entry.get() and password_entry.get() != '':
            deleting_frame(number,number_1)
            check_authentication(email_entry.get() , password_entry.get())
            show_once = 0
            show_another = 0
            number = 0
            number_1 = 0

        elif "@yahoo.com" in email_entry.get() and password_entry.get() != '':
            deleting_frame(number,number_1)
            check_authentication(email_entry.get() , password_entry.get())
            show_once = 0
            show_another = 0

        elif "@icloud.com" in email_entry.get() and password_entry.get() != '':
            deleting_frame(number,number_1)
            check_authentication(email_entry.get() , password_entry.get())
            show_once = 0
            show_another = 0

        elif "@email.com" in email_entry.get():
            pass

        elif "@gmail.com" in email_entry.get() and password_entry.get() == "":
            pass

        elif "@yahoo.com" in email_entry.get() and password_entry.get() == "":
            pass

        elif "@icloud.com" in email_entry.get() and password_entry.get() == "":
            pass

        else:
            if ("@gmail.com" not in email_entry.get() or email_entry.get() == "") and show_once < 1:
                display_error()
                show_once = 1
            elif "@yahoo.com" not in email_entry.get() and show_once < 1:
                display_error()
                show_once = 1
            elif "@icloud.com" not in email_entry.get() and show_once < 1:
                display_error()
                show_once = 1
            
            if number >= 1 and number_1 >= 1:
                root.geometry("630x460")
            elif number >= 1 and number_1 == 0:
                root.geometry("630x460")
            elif number == 0 and number_1 >= 1:
                root.geometry("630x300")


    def confirm():
        global show_another

        if (email_entry.get() == "" or email_entry.get() == "example@email.com") and show_another < 1:
           repeat()
           root.geometry("630x460")
           show_another = 1

        elif password_entry.get() == "" and show_another < 1:
            repeat()
            root.geometry("630x460")
            show_another = 1
        else:
            second_confirm()

    
    def new_user():
        root_2 = Toplevel()
        root_2.geometry("1000x280")

        database = sqlite3.connect("User_Details.db")
        database_cursor = database.cursor()

        def user_info():

            global new_exterior_frame_1
            global new_exterior_frame_2
            global new_exterior_frame_3
            global new_exterior_frame_4
            global new_exterior_frame_5
            global new_exterior_frame_6
            global new_exterior_frame_7
            global first_number
            global second_number
            global third_number
            global fourth_number
            global back_button
            global confirm_pass_button
            global fifth_number
            global sixth_number
            global seventh_number


            first_number = 0
            second_number = 0
            third_number = 0
            fourth_number = 0
            fifth_number = 0
            sixth_number = 0
            seventh_number = 0

            # Create a label:
            details_label = Label(root_2 , text = 'Details' , bg = "darkgrey" , font = (None , 15) , anchor = E)
            details_label.grid(row = 0 , column = 0 , columnspan = 3 , sticky = W + E )

            # Let's define some tkinter variables:
            first_name_str = StringVar()
            first_name_str.set("Enter First Name..")

            last_name_str = StringVar()
            last_name_str.set("Enter Last Name..")

            new_passvar = StringVar()

            new_emailvar = StringVar()
            new_emailvar.set("example@email.com")

            new_email_menu = StringVar()
            new_email_menu.set("@gmail.com")

            new_password_menu = StringVar()
            new_password_menu.set("show")


            new_options_1 = [
                "@gmail.com" , 
                "@yahoo.com" ,
                "@icloud.com" , 
                "clear"
            ]

            new_options_2 = [
                "-show-" , 
                "-hide-" , 
                "clear"
            ]

            new_invalid_option = [
                "*Invalid Email OR Password:",
                "   -Please Make Sure You've Given A Valid Email Address-",
                "   -Please Make Sure The Password Is in Between 8-50 Characters Maximum",
                "   -Your Password Must Also Contain Upper-Case Letters And Numbers"
            ]


            def highlight_back_button(event):
                global back_button
                back_button.config(bg = "red" , fg = "snow" , font = ("Helvetica" , 11 , "bold" , "underline"))
                
            def un_highlight_back_button(event):
                global back_button
                back_button.config(fg = "black" , bg = "gainsboro" , font = ("Helvetica" , 11))

            def highlight_new_confirm_button(event):
                new_confirm_button.config(fg = "blue" , bg = "springgreen" , font = ("Helvetica" , 11 , "bold" , "underline"))

            def un_highlight_new_confirm_button(event):
                new_confirm_button.config(fg = "black" , bg = "gainsboro" , font = ("Helvetica" , 11))


            def highlight_confirm_pass_button(event):
                global confirm_pass_button
                confirm_pass_button.config(fg = "blue" , bg = "springgreen" , font = ("Helvetica" , 11 , "bold" , "underline"))

            def un_highlight_confirm_pass_button(event):
                global confirm_pass_button
                confirm_pass_button.config(fg = "black" , bg = "gainsboro" , font = ("Helvetica" , 11))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            '''
This block right here is going to govern our event functions, meaning that when an event takes place one of these functions will be executed.
You may wonder why won't we just pack it all into one main function? well that would result in an error or and exception to be precise,
this exception will cause our program to delete the non-default contents of our Entry widget when one is in focus.
            '''
            def new_focus_next_window_last(event):

                event.widget.tk_focusNext().focus()
                
                # This method will first check if the contents of our last_name widget or email_address,
                # delete the default contents and config the foreground to the colour "black"
                # However it will not empty out the widget if it doesn't have any of it's default contents

                if "Enter Last Name.." in last_name.get():               
                    event.widget.tk_focusNext().delete(0 , END)

                event.widget.tk_focusNext().config(fg = "black")

                return("break")


            def new_focus_next_window_email(event):

                event.widget.tk_focusNext().focus()

                if "example@email.com" in email_address.get():
                    event.widget.tk_focusNext().delete(0 , END)

                event.widget.tk_focusNext().config(fg = "black")

                return("break")


            def new_focus_next_window_pass(event):

                event.widget.tk_focusNext().focus()

                if user_password.get() == "":
                    event.widget.tk_focusNext().delete(0 , END)

                event.widget.tk_focusNext().config(fg = "black")

                return("break")


            def new_focus_prev_window_first(event):

                event.widget.tk_focusPrev().focus()

                if "Enter First Name.." in first_name.get() :
                    event.widget.tk_focusPrev().delete(0 , END)

                event.widget.tk_focusPrev().config(fg = "black")

                return("break")


            
            def new_focus_prev_window_last(event):

                event.widget.tk_focusPrev().focus()

                if "Enter Last Name.." in  last_name.get() :
                    event.widget.tk_focusPrev().delete(0 , END)

                event.widget.tk_focusPrev().config(fg = "black")

                return("break")


            def new_focus_prev_window_email(event):

                event.widget.tk_focusPrev().focus()

                if "example@email.com" in email_address.get() : 
                    event.widget.tk_focusPrev().delete(0 , END)

                event.widget.tk_focusPrev().config(fg = "black")

                return("break")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            def clear_first():
            
                first_name.delete(0 , END)
                first_name.config(fg = "black")

            def clear_last():

                last_name.delete(0 , END)
                last_name.config(fg = "black")



            def first_name_click(event):
                if first_name.get() == "Enter First Name..":
                    event.widget.delete(0 , END)
                    first_name.config(fg = "black")

            def last_name_click(event):
                if last_name.get() == "Enter Last Name..":
                    event.widget.delete(0 , END)
                    last_name.config(fg = "black")
            
            def email_address_click(event):
                if email_address.get() == "example@email.com":
                    event.widget.delete(0 , END)
                    email_address.config(fg = "black")

            def user_password_click(event):
                if first_name.get() == "":
                    first_name.config(fg = "grey")
                    first_name.insert(0 , "Enter First Name..")
                    
                if last_name.get() == "":
                    last_name.config(fg  = "grey")
                    last_name.insert(0 , "Enter Last Name..")
                    
                if email_address.get() == "":
                    email_address.config(fg = "grey")
                    email_address.insert(0 , "example@email.com")
                    
            def addresses(event):

                if new_email_menu.get() != "clear" and email_address.get() != "example@email.com":
                    email_address.config(fg = "black")
                    user_name = email_address.get()
                    user_address = new_email_menu.get()
                    new_email = user_name + user_address
                    for item in new_email.split("@"):
                        new_email = item + new_email_menu.get()
                        break
                    email_address.delete(0 , END)
                    email_address.insert(0 , new_email)

                elif email_address.get() == "example@email.com":
                    email_address.delete(0 , END)
                    email_address.config(fg = "black")
                    email_address.insert(0 , new_email_menu.get())

                elif "example@email.com" in email_address.get():
                    new_email = ""
                    for item in email_address.get().split("example@email.com"):
                        new_email += item 
                    email_address.delete(0 , END)
                    email_address.insert(0 , new_email)

                else:
                    email_address.delete(0 , END)

            def user_password_show(event):
                if new_password_menu.get() == "-show-":
                    user_password.config(show = "")
                    new_password_menu.set("show")

                elif new_password_menu.get() == "-hide-":
                    user_password.config(show = "\u2022")
                    new_password_menu.set("hide")

                else:
                    user_password.delete(0 , END)

            def display_first_error():

                global new_exterior_frame_1
                global first_number

                new_exterior_frame_1 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_1.grid(row = 2 , column = 1 , pady = (0 , 10) , sticky = N)

                new_interior_frame_1 = Frame(new_exterior_frame_1 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_1.grid(row = 0 , column = 0 , columnspan = 3 , padx = 1 , pady = 1 , sticky = W + E)

                info_1 = Label(new_interior_frame_1 , text = "Please Make Sure To Enter Your First Name!" , fg = "red" , bg = "pink" , font = ("Helvetica" , 10 , "bold") , anchor = CENTER)
                info_1.pack(padx = 38)  # 38

                first_number = 1

            def display_last_error():

                global new_exterior_frame_2
                global second_number

                new_exterior_frame_2 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_2.grid(row = 4 , column = 1 , pady = (0 , 10) , sticky = N)

                new_interior_frame_2 = Frame(new_exterior_frame_2 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_2.grid(row = 0 , column = 0 , columnspan = 3 , padx = 1 , pady = 1 , sticky = W + E)

                info_2 = Label(new_interior_frame_2 , text = "Please Make Sure To Enter Your Last Name.." , fg = "red" , bg = "pink" , font = ("Helvetica" , 10 , "bold") , anchor = CENTER)
                info_2.pack(padx = 36)  # 36
                
                second_number = 1

            def email_error():
                
                global new_exterior_frame_3
                global third_number

                new_exterior_frame_3 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_3.grid(row = 6 , column = 1 , pady = (0 , 10) , sticky = N)

                new_interior_frame_3 = Frame(new_exterior_frame_3 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_3.grid(row = 0 , column = 0 , columnspan = 3 , padx = 1 , pady = 1 , sticky = W + E)

                info_3 = Label(new_interior_frame_3 , text = "Please Attach A Valid Email Address.." , fg = "red" , bg = "pink" , font = ("Helvetica" , 10 , "bold") , anchor = CENTER)
                info_3.pack(padx = 59)
                
                third_number = 1

            def display_final_error():
                
                global new_exterior_frame_4
                global fourth_number

                new_exterior_frame_4 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_4.grid(row = 8 , column = 1 , pady = (0 , 20) , sticky = W)

                new_interior_frame_4 = Frame(new_exterior_frame_4 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_4.grid(row = 0 , column = 0 , columnspan = 3 , padx = 1 , pady = 1 , sticky = W + E)
                for num , text in enumerate(new_invalid_option):
                    info_4 = Label(new_interior_frame_4 , text = text , fg = "red" , bg = "pink" , font = ("Helvetica" , 9 , "bold") , anchor = W)
                    info_4.grid(row = num , column = 0 , sticky = W , pady = (5 , 10) , padx = (20 , 24))
                
                fourth_number = 1

            def display_confirm_error():

                global new_exterior_frame_5
                global fifth_number

                new_exterior_frame_5 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_5.grid(row = 9 , column = 1 , sticky = N , pady = (0 , 20))

                new_interior_frame_5 = Frame(new_exterior_frame_5 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_5.grid(row = 0 , column = 0 , columnspan = 3 , sticky = W + E , padx = 1 , pady = 1)

                info_5 = Label(new_interior_frame_5 , text = "Wrong Password!" , fg = "red" , bg = "pink" , font = ("Helvetica" , 10 , "bold") , anchor = CENTER)
                info_5.pack(padx = 123)

                fifth_number = 1

            def display_upper_case_error():
                
                global new_exterior_frame_6
                global sixth_number

                new_exterior_frame_6 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_6.grid(row = 9 , column = 1 , sticky = N , pady = (0 , 20))

                new_interior_frame_6 = Frame(new_exterior_frame_6 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_6.grid(row = 0 , column = 0 , sticky = W + E , padx = 1 , pady = 1)

                info_6 = Label(new_interior_frame_6 , text = "Please Insert A Upper-Case Letter.." , fg = "red" , bg = "pink" , font = ("Helvetica", 10 , "bold") , anchor = CENTER)
                info_6.pack(ipadx = 68)

                sixth_number = 1


            def display_number_error():

                global new_exterior_frame_7
                global seventh_number

                new_exterior_frame_7 = Frame(root_2 , width = 56 , height = 21 , bg = "red")
                new_exterior_frame_7.grid(row = 9 , column = 1 , sticky = N , pady = (0 , 20))

                new_interior_frame_7 = Frame(new_exterior_frame_7 , width = 55 , height = 20 , bg = "pink")
                new_interior_frame_7.grid(row = 0 , column = 0 , sticky = W + E , padx = 1 , pady = 1)

                info_7 = Label(new_interior_frame_7 , text = "Please Insert Some Digits.." , fg = "red" , bg = "pink" , font = ("Helvetica", 10 , "bold") , anchor = CENTER)
                info_7.pack(ipadx = 93)

                seventh_number = 1



            def deleting_exterior_frames():

                global first_number
                global second_number
                global third_number
                global fourth_number
                global fifth_number
                global sixth_number
                global seventh_number

                if first_number == 2:
                    new_exterior_frame_1.destroy()
                    first_number = 0

                if second_number == 2:
                    new_exterior_frame_2.destroy()
                    second_number = 0

                if third_number == 2:
                    new_exterior_frame_3.destroy()
                    third_number = 0

                if fourth_number == 2:
                    new_exterior_frame_4.destroy()
                    fourth_number = 0

                if fifth_number == 2:
                    new_exterior_frame_5.destroy()
                    fifth_number = 0

                if sixth_number == 2:
                    new_exterior_frame_6.destroy()
                    sixth_number = 0

                if seventh_number == 2:
                    new_exterior_frame_7.destroy()
                    seventh_number = 0


            def add_into_database():
                
                global confirm_password
                global fifth_number

                database = sqlite3.connect("User_Details.db")
                database_cursor = database.cursor()

                if confirm_password.get() != user_password.get():
                    display_confirm_error()
                    fifth_number = 2
                    resize_function()

                else:
                    go_back()

                    # Now the checking program starts to see if the user already exists in our database:

                    database_cursor.execute(""" SELECT * , oid FROM Details""")
                    database_records = database_cursor.fetchall()

                    for record in database_records:
                        if (first_name.get() or last_name.get() or user_password.get()) and email_address.get() in record:
                            print("user already exist")
                            user_info()
                            break
                    else:
                        
                        user_info()

                database.commit()
                database.close()
                

            def go_back():

                global back_button
                global confirm_pass_button
                global confirm_password
                global confirm_password_label
                global astrixe_6

                deleting_exterior_frames()
                resize_function()

                first_name.config(state = NORMAL)
                first_name.config(state = NORMAL)
                last_name.config(state = NORMAL)
                email_address.config(state = NORMAL)
                user_password.config(state = NORMAL , show = "")
                new_password_menu.set("show")


                user_password.grid_configure(pady = (0 , 17))
                user_password_label.grid_configure(pady = (0 , 17))
                astrixe_5.grid_configure(pady = (0 , 17))
                password_drop_box.grid_configure(pady = (0 , 17))


                confirm_password.grid_forget()
                confirm_pass_button.grid_forget()
                confirm_password_label.grid_forget()
                astrixe_6.grid_forget()
                back_button.grid_forget()

                new_confirm_button.grid()  # This statement right here will bring back our removed confirm button widget.
                


            def confirm_check():

                global first_number
                global second_number
                global third_number
                global fourth_number
                global back_button
                global confirm_password
                global confirm_pass_button
                global confirm_password_label
                global astrixe_6

                root_2.geometry("1000x310") # Make sure to change the parents widget's geometry

                # Disable all Entries:
                
                first_name.config(state = DISABLED)
                last_name.config(state = DISABLED)
                email_address.config(state = DISABLED)
                user_password.config(state = DISABLED , show = "\u2022") # Bullet symbol

                user_password.grid_configure(pady = (0 , 10))
                user_password_label.grid_configure(pady = (0 , 10))
                astrixe_5.grid_configure(pady = (0 , 10))
                password_drop_box.grid_configure(pady = (0 , 10))
                new_confirm_button.grid_remove()

                # Add a new confirm password entry:

                confirm_password = Entry(root_2 , width = 60 , fg = "black")
                confirm_password.focus() # This command will focus our cursor onto our confirm_password widget
                confirm_password.grid(row = 8 , column = 1 , pady = (0 , 17) , sticky = W + E)

                confirm_password_label = Label(root_2 , text = "Confirm Password: " , font = ("Helvetica" , 11))
                confirm_password_label.grid(row = 8 , column = 0 , pady = (0,17) , padx = 5 , sticky = E)

                astrixe_6 = Label(root_2 , text = "*" , fg = "red" , font = ("Helvetica" , 11))
                astrixe_6.grid(row = 8 , column = 0 , pady = (0 , 17) , padx = (0 , 138) , sticky = E)

                # Create our 'Back' Button:
                confirm_pass_button = Button(root_2 , text = "Confirm" , font = ("Helvetica" , 11) , bg = "gainsboro" , command = add_into_database , width = 10)
                confirm_pass_button.bind("<Enter>" , highlight_confirm_pass_button)
                confirm_pass_button.bind("<Leave>" , un_highlight_confirm_pass_button)
                confirm_pass_button.grid(row = 10 , column = 1 , sticky = E , pady = (10 , 25) , ipadx = 20)

                back_button = Button(root_2 , text = "Go Back" , fg = "black" , bg = "gainsboro" , font = ("Helvetica" , 11) , command = go_back , width = 10)
                back_button.bind("<Enter>" , highlight_back_button)
                back_button.bind("<Leave>" , un_highlight_back_button)
                back_button.grid(row = 10 , column = 1 , sticky = W , pady = (10 , 25) , ipadx = 20)


                print(first_name.get() , last_name.get() , email_address.get() , user_password.get())


            
            def new_confirm():

                global first_number
                global second_number
                global fourth_number
                global third_number
                global sixth_number
                global seventh_number
                
                
                if (first_name.get() == "" or first_name.get() == "Enter First Name..") and first_number <= 1:
                    display_first_error()
                    first_number = 2
                    resize_function()
                
                if (last_name.get() == "" or last_name.get() == "Enter Last Name..") and second_number <= 1:
                    display_last_error()
                    second_number = 2
                    resize_function()

                if (email_address.get() == "" or email_address.get() == "example@email.com") and fourth_number <= 1:
                    display_final_error()
                    fourth_number = 2
                    resize_function()

                elif (user_password.get() == "" or (len(user_password.get()) < 8 or len(user_password.get()) >= 50)) and fourth_number <= 1:
                    display_final_error()
                    fourth_number = 2
                    resize_function()
                    
                else:
                    if "@gmail.com" in email_address.get() or "@yahoo.com" in email_address.get() or "@icloud.com" in email_address.get():
                        if user_password.get() != "" and (len(user_password.get()) >= 8 and len(user_password.get()) <= 50):
                            if (first_name.get() == "" or first_name.get() == "Enter First Name..") or (last_name.get() == "" or last_name.get() == "Enter Last Name.."):
                                pass
                            else:
                                boolean = True
                                while boolean:
                                    for character in range(1 , 27):
                                        if chr(character + 64) in user_password.get():
                                            boolean = False
                                            break
                                    else:
                                        deleting_exterior_frames()
                                        resize_function()
                                        display_upper_case_error()
                                        sixth_number = 2
                                        resize_function()
                                        break
                                    for numbers in range(0,10):
                                        if str(numbers) in user_password.get():
                                            boolean = False
                                            break
                                    else:
                                        deleting_exterior_frames()
                                        resize_function()
                                        display_number_error()
                                        seventh_number = 2
                                        resize_function()
                                        break
                                    
                                else:
                                    #confirm_check    <-- by removing this we are making sure that our program is executing line by line AFTER removing our exterior frames and resizing our program.
                                    deleting_exterior_frames()
                                    resize_function()
                                    confirm_check()
                        else:
                            pass
                    else:
                        email_error()
                        third_number = 2
                        resize_function()

        
            def resize_function():

                global first_number
                global second_number
                global third_number
                global fourth_number
                global fifth_number
                global sixth_number
                global seventh_number

                # Logic to display certain widgets:

                if first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x580")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x580")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x580")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x417")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x417")

                elif first_number == 2 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x380")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x520")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x380")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x380")

                elif first_number == 2 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x350")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x520")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x390")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x390")

                elif first_number == 2 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x350")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x525")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x525")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x480")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x345")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x345")

                elif first_number == 2 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x310")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x550")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x520")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x390")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x390")

                elif first_number == 0 and second_number == 2 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x350")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x525")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x525")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x480")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x345")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x345")

                elif first_number == 0 and second_number == 2 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x310")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x525")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x525")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x480")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x345")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x345")

                elif first_number == 0 and second_number == 0 and third_number == 2 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x310")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x480")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x480")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 2 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x445")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 2 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x317")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 2 and fifth_number == 0:
                    root_2.geometry("1000x317")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 0:
                    root_2.geometry("1000x280")

                elif first_number == 0 and second_number == 0 and third_number == 0 and fourth_number == 0 and sixth_number == 0 and seventh_number == 0 and fifth_number == 2:
                    root_2.geometry("1000x350")

            # Creating Entry widget:

            first_name = Entry(root_2 , width = 80 , textvariable = first_name_str , fg = "grey")
            first_name.bind("<Button-1>" , first_name_click)
            first_name.bind("<Return>" , new_focus_next_window_last)
            first_name.bind("<Down>" , new_focus_next_window_last)
            first_name.grid(row = 1 , column = 1 , pady = (25 , 10) , sticky = W+E , ipady = 1)

            #first_name_clear = Button(root_2 , text = "Clear" , font = ("Helvetica" , 9) , command = clear_first)
            #first_name_clear.grid(row = 1 , column = 2 , pady = (25 , 10) , sticky = W  , padx = (10 , 0) , ipadx = 15)

            last_name = Entry(root_2 , width = 60 , textvariable = last_name_str , fg = "grey")
            last_name.bind("<Button-1>" , last_name_click)
            last_name.bind("<Return>" , new_focus_next_window_email)
            last_name.bind("<Up>" , new_focus_prev_window_first)
            last_name.bind("<Down>" , new_focus_next_window_email)
            last_name.grid(row = 3 , column = 1 , pady = (0 , 10) , sticky = W+E , ipady = 1)

            #last_name_clear = Button(root_2 , text = "Clear" , font = ("Helvetica" , 9) , command = clear_last)
            #last_name_clear.grid(row = 3 , column = 2 , pady = (0 , 10) , sticky = W  , padx = (10 , 0) , ipadx = 15)

            email_address = Entry(root_2 , width = 60 , textvariable = new_emailvar , fg = "grey")
            email_address.bind("<Button-1>" , email_address_click)
            email_address.bind("<Return>" , new_focus_next_window_pass)
            email_address.bind("<Up>" , new_focus_prev_window_last)
            email_address.bind("<Down>" , new_focus_next_window_pass)
            email_address.grid(row = 5 , column = 1 , pady = (0 , 10) , sticky = W+E , ipady = 1)

            email_drop_box = OptionMenu(root_2 , new_email_menu ,*new_options_1 , command = addresses)
            email_drop_box.grid(row = 5 , column = 2 , sticky = W , padx = (10 , 0) , pady = (0 , 10))

            user_password = Entry(root_2 , width = 60 , textvariable = new_passvar , fg = "black")
            user_password.bind("<Button-1>" , user_password_click)
            #user_password.bind("<Return>" , new_focus_next_window)
            user_password.bind("<Up>" , new_focus_prev_window_email)
            user_password.grid(row = 7 , column = 1 , pady = (0 , 17) , sticky = W+E , ipady = 1)

            password_drop_box = OptionMenu(root_2 , new_password_menu , *new_options_2 , command = user_password_show)
            password_drop_box.grid(row = 7 , column = 2 , padx = (10 , 0) , pady = (0 , 17) , stick = W)

            # Creating Entry labels:

            first_name_label = Label(root_2 , text = "First Name: " , font = ("Helvetica" , 11))
            first_name_label.grid(row = 1 , column = 0 , pady = (25 , 10) , padx = 5 , sticky = E)

            astrixe_1 = Label(root_2 , text = "*" , font = ("Helvetica" , 11) , fg = "red")
            astrixe_1.grid(row = 1 , column = 0 , pady = (25 , 10) , sticky = E , padx = (0,90))

            last_name_label = Label(root_2 , text = "Last Name: " , font = ("Helvetica" , 11))
            last_name_label.grid(row = 3 , column = 0 , pady = (0 , 10) , padx = 5 , sticky = E)

            astrixe_2 = Label(root_2 , text = "*" , font = ("Helvetica" , 11) , fg = "red")
            astrixe_2.grid(row = 3 , column = 0 , pady = (0 , 10) , sticky = E , padx = (0,88))

            email_address_label = Label(root_2 , text = "Email Adress: " , font = ("Helvetica" , 11))
            email_address_label.grid(row = 5 , column = 0 , pady = (0 , 10) , padx = 5 , sticky = E)

            astrixe_3 = Label(root_2 , text = "*" , font = ("Helvetica" , 11) , fg = "red")
            astrixe_3.grid(row = 5 , column = 0 , pady = (0 , 10) , sticky = E , padx = (0,105))

            user_password_label = Label(root_2 , text = "Password: " , font = ("Helvetica" , 11))
            user_password_label.grid(row = 7 , column = 0 , pady = (0 , 17) , padx = 5 , sticky = E)

            astrixe_5 = Label(root_2 , text = "*" , font = ("Helvetica" , 11) , fg = "red")
            astrixe_5.grid(row = 7 , column = 0 , pady = (0 , 17) , sticky = E , padx = (0,83))

            # Buttons:

            new_confirm_button = Button(root_2 , text = "Confirm" , font = ("Helvetica" , 11) , bg = "gainsboro" , command = new_confirm , width = 10)
            new_confirm_button.bind("<Enter>" , highlight_new_confirm_button)
            new_confirm_button.bind("<Leave>" , un_highlight_new_confirm_button)
            new_confirm_button.grid(row = 10 , column = 1 , pady = (10 , 25) , sticky = N , ipadx = 20)

            #display_first_error()
            #display_last_error()
            #email_error()
            #display_final_error()


        user_info()

        database.commit()
        database.close()

        root_2.grid_columnconfigure(0 , weight = 1)
        root_2.grid_columnconfigure(2 , weight = 1)

        
        root_2.mainloop()
        
        

    name_label = Label(root , text = "Log-in" , font = (None , 15) , bg = "darkgrey" , anchor = E)
    name_label.grid(row = 0 , column = 0 , columnspan = 3 , sticky = W + E , ipadx = 100)

    # Email:

    email_label = Label(root , text = "Email Address: " , font = (None , 11))
    email_label.grid(row = 1 , column = 1 , pady = (25 , 5) , sticky = W)

    astrixe = Label(root , text = "*" , font = (None , 11) , fg = "red")
    astrixe.grid(row = 1 , column = 0 , pady = (25 , 5) , sticky = E)

    email_entry = Entry(root , width = 60 , textvariable = emailvar , fg = "grey")
    email_entry.bind("<Button-1>" , email_click)
    email_entry.bind("<Return>" , focus_next_window)
    email_entry.grid(row = 2 , column = 1 , pady = (0 , 10) , sticky = W)

    email_drop_box = OptionMenu(root , email_menu , *options_1 , command = addresses)
    email_drop_box.grid(row = 2 , column = 2 , padx = (10,0) , pady = (0 , 10) , sticky = W)

    # Password:

    password_label = Label(root , text = "Password: " , font = (None , 11))
    password_label.grid(row = 4 , column = 1 , padx = (0 , 10) , sticky = W)

    password_entry = Entry(root , width = 60 , textvariable = passvar , fg = "black")
    password_entry.bind("<Button-1>" , pass_click)
    password_entry.grid(row = 5 , column = 1 , pady = (0 , 25) , sticky = W)

    astrixe_2 = Label(root , text = "*" , font = (None , 11) , fg = "red")
    astrixe_2.grid(row = 4 , column = 0  , sticky = E) 

    pass_drop_box = OptionMenu(root , password_menu ,*options_2 , command = show_pass)
    pass_drop_box.grid(row = 5 , column = 2 , padx = (10,0) , pady = (0 , 25) , sticky = W )

    # Buttons:
    confirm_button = Button(root , text = "Confirm" , font = ("Helvetica" , 11) , command = confirm , width = 10 , bg = "gainsboro")
    confirm_button.bind("<Enter>" , highlight_confirm_button)
    confirm_button.bind("<Leave>" , un_highlight_confirm_button)
    confirm_button.grid(row = 7 , column = 1 , pady = (10,25), ipadx = 20  , sticky = SE)

    new_user_button = Button(root , text = "New User?" , font = ("Helvetica" , 11) , command = new_user , width = 10 , bg = "gainsboro")
    new_user_button.bind("<Enter>" , highlight_user_button)
    new_user_button.bind("<Leave>" , un_highlight_user_button)
    new_user_button.grid(row = 7 , column = 1 , pady = (10,25), ipadx = 20 , sticky = SW)


first_bit()

database.commit()
database.close()

root.grid_columnconfigure(0 , weight = 1)
root.grid_columnconfigure(2 , weight = 1)

root.mainloop()