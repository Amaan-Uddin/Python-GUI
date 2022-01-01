# Guessing game with GUI
 
from tkinter import *
from random import *
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
from PIL import ImageTk , Image
import time
from tkinter import Radiobutton


# First create a window:
root = Tk()
# Give it a title/name
root.title("Guessing Game")
root.geometry("660x480")
root.configure(background = "lightpink")

# Let's add an icon to it:
root.iconbitmap("visual_studio_code_icon_191771.ico")

def third_bit_hard():
    global frame_2
    global frame_3
    global list_hard
    global tries
    global answer
    global ans_label
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global button_0
    global button_eql
    global button_clear 
    global option
    global user_number
    global response
    global second_list

    # Remove the preious frames
    frame_2.grid_forget()
    frame_3.grid_forget()

    # And adjust the root geometry
    root.geometry("1013x455")
    root.minsize(width = 1013 , height = 455)
    root.maxsize(width = 1013 , height = 455)

    # Let's create our random-number:
    random_number = randrange(0 , 501)
    tries = 10     # The first value for number of tries the user takes
    option = 1    # This is for the hint function, the first hint to be displayed.
    second_list = []
    active_bg_colour = "darksalmon"

    inner_frame_1 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    inner_frame_2 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    inner_frame_3 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    #inner_frame_4 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3 )
    # IMPORTANT point: do not pack()/grid() a widget when it is assigned to a variable.
    # Also don't forget to put LabelFrame to insert a frame inside of a widget.

    inner_frame_1.configure(background = "red")
    inner_frame_2.configure(background = "lightskyblue")
    inner_frame_3.configure(background = "paleturquoise")
    #inner_frame_4.configure(background = "springgreen")

    inner_frame_1.grid(row = 0 , column = 0 , sticky = N+W , padx = 8 , pady = 8)
    inner_frame_2.grid(row = 0 , column = 1 , sticky = N , padx = 8 , pady = 8)
    inner_frame_3.grid(row = 0 , column = 2 , sticky = N+E , padx = 8 , pady = 8)
    #inner_frame_4.grid(row = 1 , column = 0 , sticky = S+W , padx = 8 , pady = 8)

    Label(inner_frame_1 , text = "Info:" , fg = "white" , bg = "red" , font = (None , 14)).grid(row = 0 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
    for item in range(len(list_easy)):
        Label(inner_frame_1 , text = list_hard[item] , fg = "white" , bg = "red" , font = (None , 11)).grid(row = item + 1 , column = 0 , columnspan = 3 ,sticky = W , padx = 5 , pady = 6)

    Label(inner_frame_1 , text = "Number of Guesses left:" , fg = "white" , bg = "red" , font = (None , 18)).grid(row = 6 , column = 0 , padx = 7 , pady = 15 , sticky = W)
    response = Label(inner_frame_1 , text = str(tries) , fg = "white" , bg = "red" , font = (None , 18))
    response.grid(row = 6 , column = 1 , padx = 7 , pady = 15 , sticky = W)

    ans_label = Label(inner_frame_1 , text = "The Answer is :" , fg = "white" , bg = "red" , font = (None , 19))
    ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)

    answer = Label(inner_frame_1 , text = " " , bg = "red" , font = (None , 18))
    answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)

    hints = Label(inner_frame_3 , text = "Hint:" , fg = "white" , bg = "paleturquoise" , font = (None , 11))
    hints.grid(row = 1 , column = 0 , sticky  = W , padx = 10 , pady = 7)

    def choose_hint():
        if random_number % 2 == 0:
            hint_1 = "Number is an Even"
        else:
            hint_1 = "Number is Odd"

        hint_2 = f"Last digit of the number is {random_number % 10}"

        for item in str(random_number):
            hint_3 = f"First digit of the number is {item}"
            break

        mid = int(random_number/2)
        toss = 0
        for item in range(2 , mid+1):
            if random_number % item == 0:
                toss = 1
                break
            else:
                toss = 0
        if toss == 0:
            hint_4 = "It's a prime number"
        else:
            hint_4 = "It's not a prime number" 

        hint_5 = f"It is in the range {random_number - randrange(7,15)} and {random_number + randrange(7,15)}"

        list_of_hints = [hint_1 , hint_2 , hint_3 , hint_4, hint_5]

        return list_of_hints


    def number_of_tries():
        global tries
        global ans_label
        global answer
        global user_number
        global button_1
        global button_2
        global button_3
        global button_4
        global button_5
        global button_6
        global button_7
        global button_8
        global button_9
        global button_0
        global button_eql
        global button_clear
        global response

        response.grid_forget()

        response = Label(inner_frame_1 , text = str(tries-1) , fg = "white" , bg = "red" , font = (None , 18))
        tries -= 1
        response.grid(row = 6 , column = 1 , padx = 7 , pady = 15 , sticky = W)

        if tries == 0:
            if int(user_number) == random_number:
                ans_label.grid_forget()
                answer.grid_forget()
                button_1.grid_forget()
                button_2.grid_forget()
                button_3.grid_forget()
                button_4.grid_forget()
                button_5.grid_forget()
                button_6.grid_forget()
                button_7.grid_forget()
                button_8.grid_forget()
                button_9.grid_forget()
                button_0.grid_forget()
                button_eql.grid_forget()
                button_clear.grid_forget()

                ans_label = Label(inner_frame_1 , text = "Congratulations.." , fg = "white" , bg = "red" , font = (None , 19))
                ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)

                answer = Label(inner_frame_1 , text = "You Won" , fg = "white" , bg = "red" , font = (None , 19))
                answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                #number_of_tries()

                button_1 = Button(inner_frame_2 , text = "1", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(1) , state = DISABLED)
                button_2 = Button(inner_frame_2 , text = "2", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(2) , state = DISABLED)
                button_3 = Button(inner_frame_2 , text = "3", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(3) , state = DISABLED)
                button_4 = Button(inner_frame_2 , text = "4", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(4) , state = DISABLED)
                button_5 = Button(inner_frame_2 , text = "5", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(5) , state = DISABLED)
                button_6 = Button(inner_frame_2 , text = "6", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(6) , state = DISABLED)
                button_7 = Button(inner_frame_2 , text = "7", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(7) , state = DISABLED)
                button_8 = Button(inner_frame_2 , text = "8", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(8) , state = DISABLED)
                button_9 = Button(inner_frame_2 , text = "9", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(9) , state = DISABLED)
                button_0 = Button(inner_frame_2 , text = "0", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(0) , state = DISABLED)
                button_eql = Button(inner_frame_2 , text = "=" , font = (None , 14) , padx = 90 , pady = 15 , command = lambda:equal() , state = DISABLED)
                button_clear = Button(inner_frame_2 , text = "Clear" , font = (None , 14) , padx = 73 , pady = 15 , command = lambda:clear() , state = DISABLED)

                button_7.grid(row = 1 , column = 0 , padx = 5 , pady = 5)
                button_8.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
                button_9.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

                button_4.grid(row = 2 , column = 0 , padx = 5 , pady = 5)
                button_5.grid(row = 2 , column = 1 , padx = 5 , pady = 5)
                button_6.grid(row = 2 , column = 2 , padx = 5 , pady = 5)

                button_3.grid(row = 3 , column = 0 , padx = 5 , pady = 5)
                button_2.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
                button_1.grid(row = 3 , column = 2 , padx = 5 , pady = 5)
                button_0.grid(row = 4 , column = 0 , padx = 5 , pady = 5)

                button_eql.grid(row = 5 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E)
                button_clear.grid(row = 4 ,column = 1 , columnspan = 2 , padx = 5 , pady = 5)

            else:
                ans_label.grid_forget()
                answer.grid_forget()
                
                ans_label = Label(inner_frame_1 , text = "Sorry, you ran out of guesses " , fg = "white" , bg = "red" , font = (None , 18))
                answer = Label(inner_frame_1 , text = "Press 'Retry' if you wanna play again." , fg = "white" , bg = "red" , font = (None , 17))
                ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)


                button_1 = Button(inner_frame_2 , text = "1", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(1) , state = DISABLED)
                button_2 = Button(inner_frame_2 , text = "2", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(2) , state = DISABLED)
                button_3 = Button(inner_frame_2 , text = "3", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(3) , state = DISABLED)
                button_4 = Button(inner_frame_2 , text = "4", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(4) , state = DISABLED)
                button_5 = Button(inner_frame_2 , text = "5", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(5) , state = DISABLED)
                button_6 = Button(inner_frame_2 , text = "6", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(6) , state = DISABLED)
                button_7 = Button(inner_frame_2 , text = "7", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(7) , state = DISABLED)
                button_8 = Button(inner_frame_2 , text = "8", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(8) , state = DISABLED)
                button_9 = Button(inner_frame_2 , text = "9", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(9) , state = DISABLED)
                button_0 = Button(inner_frame_2 , text = "0", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(0) , state = DISABLED)
                button_eql = Button(inner_frame_2 , text = "=" , font = (None , 14) , padx = 90 , pady = 15 , command = lambda:equal() , state = DISABLED)
                button_clear = Button(inner_frame_2 , text = "Clear" , font = (None , 14) , padx = 73 , pady = 15 , command = lambda:clear() , state = DISABLED)

                button_7.grid(row = 1 , column = 0 , padx = 5 , pady = 5)
                button_8.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
                button_9.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

                button_4.grid(row = 2 , column = 0 , padx = 5 , pady = 5)
                button_5.grid(row = 2 , column = 1 , padx = 5 , pady = 5)
                button_6.grid(row = 2 , column = 2 , padx = 5 , pady = 5)

                button_3.grid(row = 3 , column = 0 , padx = 5 , pady = 5)
                button_2.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
                button_1.grid(row = 3 , column = 2 , padx = 5 , pady = 5)
                button_0.grid(row = 4 , column = 0 , padx = 5 , pady = 5)

                button_eql.grid(row = 5 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E)
                button_clear.grid(row = 4 ,column = 1 , columnspan = 2 , padx = 5 , pady = 5)
    

    entry = Entry(inner_frame_2 , bg = "white" , width = 40)
    entry.grid(row = 0 , column = 0 , columnspan = 3 , sticky = W+E , padx = 3 , pady = 10)

    def select(number):
        current_number = entry.get()       # Here we are trying to store the first number in a temperory variable.
        entry.delete(0 , END)              # Delete everything in the entry block.
        entry.insert(0 , str(current_number) + str(number))

    def equal():
        try:
            global answer
            global ans_label
            global button_1
            global button_2
            global button_3
            global button_4
            global button_5
            global button_6
            global button_7
            global button_8
            global button_9
            global button_0
            global button_eql
            global button_clear
            global user_number   
            
            user_number = entry.get()
            entry.delete(0 , END)
            if int(user_number) == random_number:
                ans_label.grid_forget()
                answer.grid_forget()
                button_1.grid_forget()
                button_2.grid_forget()
                button_3.grid_forget()
                button_4.grid_forget()
                button_5.grid_forget()
                button_6.grid_forget()
                button_7.grid_forget()
                button_8.grid_forget()
                button_9.grid_forget()
                button_0.grid_forget()
                button_eql.grid_forget()
                button_clear.grid_forget()

                ans_label = Label(inner_frame_1 , text = "Congratulations.." , fg = "white" , bg = "red" , font = (None , 19))
                ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)

                answer = Label(inner_frame_1 , text = "You Won" , fg = "white" , bg = "red" , font = (None , 19))
                answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                number_of_tries()

                button_1 = Button(inner_frame_2 , text = "1", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(1) , state = DISABLED)
                button_2 = Button(inner_frame_2 , text = "2", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(2) , state = DISABLED)
                button_3 = Button(inner_frame_2 , text = "3", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(3) , state = DISABLED)
                button_4 = Button(inner_frame_2 , text = "4", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(4) , state = DISABLED)
                button_5 = Button(inner_frame_2 , text = "5", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(5) , state = DISABLED)
                button_6 = Button(inner_frame_2 , text = "6", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(6) , state = DISABLED)
                button_7 = Button(inner_frame_2 , text = "7", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(7) , state = DISABLED)
                button_8 = Button(inner_frame_2 , text = "8", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(8) , state = DISABLED)
                button_9 = Button(inner_frame_2 , text = "9", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(9) , state = DISABLED)
                button_0 = Button(inner_frame_2 , text = "0", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(0) , state = DISABLED)
                button_eql = Button(inner_frame_2 , text = "=" , font = (None , 14) , padx = 90 , pady = 15 , command = lambda:equal() , state = DISABLED)
                button_clear = Button(inner_frame_2 , text = "Clear" , font = (None , 14) , padx = 73 , pady = 15 , command = lambda:clear() , state = DISABLED)

                button_7.grid(row = 1 , column = 0 , padx = 5 , pady = 5)
                button_8.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
                button_9.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

                button_4.grid(row = 2 , column = 0 , padx = 5 , pady = 5)
                button_5.grid(row = 2 , column = 1 , padx = 5 , pady = 5)
                button_6.grid(row = 2 , column = 2 , padx = 5 , pady = 5)

                button_3.grid(row = 3 , column = 0 , padx = 5 , pady = 5)
                button_2.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
                button_1.grid(row = 3 , column = 2 , padx = 5 , pady = 5)
                button_0.grid(row = 4 , column = 0 , padx = 5 , pady = 5)

                button_eql.grid(row = 5 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E)
                button_clear.grid(row = 4 ,column = 1 , columnspan = 2 , padx = 5 , pady = 5)

            elif int(user_number) > 500:
                    ans_label.grid_forget()
                    answer.grid_forget()
                    ans_label = Label(inner_frame_1 , text = "Sorry, " , fg = "white" , bg = "red" , font = (None , 19))
                    answer = Label(inner_frame_1 , text = "Invalid argument" , fg = "white" , bg = "red" , font = (None , 17))
                    ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                    answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)

            else:
                if int(user_number) < random_number:
                    ans_label.grid_forget()
                    answer.grid_forget()
                    ans_label = Label(inner_frame_1 , text = "The Answer is :" , fg = "white" , bg = "red" , font = (None , 19))
                    answer = Label(inner_frame_1 , text = f"Bigger than {user_number}" , fg = "white" , bg = "red" , font = (None , 18))
                    ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                    answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                    number_of_tries()
                else:
                    ans_label.grid_forget()
                    answer.grid_forget()
                    ans_label = Label(inner_frame_1 , text = "The Answer is :" , fg = "white" , bg = "red" , font = (None , 19))
                    answer = Label(inner_frame_1 , text = f"Smaller than {user_number}" , fg = "white" , bg = "red" , font = (None , 18))
                    ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                    answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                    number_of_tries()
        except:
            pass


    def clear():
        entry.delete(0 , END)


    button_1 = Button(inner_frame_2 , text = "1", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(1) , activebackground = active_bg_colour)
    button_2 = Button(inner_frame_2 , text = "2", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(2) , activebackground = active_bg_colour)
    button_3 = Button(inner_frame_2 , text = "3", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(3) , activebackground = active_bg_colour)
    button_4 = Button(inner_frame_2 , text = "4", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(4) , activebackground = active_bg_colour)
    button_5 = Button(inner_frame_2 , text = "5", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(5) , activebackground = active_bg_colour)
    button_6 = Button(inner_frame_2 , text = "6", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(6) , activebackground = active_bg_colour)
    button_7 = Button(inner_frame_2 , text = "7", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(7) , activebackground = active_bg_colour)
    button_8 = Button(inner_frame_2 , text = "8", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(8) , activebackground = active_bg_colour)
    button_9 = Button(inner_frame_2 , text = "9", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(9) , activebackground = active_bg_colour)
    button_0 = Button(inner_frame_2 , text = "0", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(0) , activebackground = active_bg_colour)
    button_eql = Button(inner_frame_2 , text = "=" , font = (None , 14) , padx = 90 , pady = 15 , command = lambda:equal() , activebackground = active_bg_colour)
    button_clear = Button(inner_frame_2 , text = "Clear" , font = (None , 14) , padx = 73 , pady = 15 , command = lambda:clear() , activebackground = active_bg_colour)

    button_7.grid(row = 1 , column = 0 , padx = 5 , pady = 5)
    button_8.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
    button_9.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

    button_4.grid(row = 2 , column = 0 , padx = 5 , pady = 5)
    button_5.grid(row = 2 , column = 1 , padx = 5 , pady = 5)
    button_6.grid(row = 2 , column = 2 , padx = 5 , pady = 5)

    button_3.grid(row = 3 , column = 0 , padx = 5 , pady = 5)
    button_2.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
    button_1.grid(row = 3 , column = 2 , padx = 5 , pady = 5)
    button_0.grid(row = 4 , column = 0 , padx = 5 , pady = 5)

    button_eql.grid(row = 5 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E)
    button_clear.grid(row = 4 ,column = 1 , columnspan = 2 , padx = 5 , pady = 5)


    def hint():
        #while True: <-- do not use while here as it will crash the program
            try:
                global option
                global second_list

                open_hint = choose_hint()
                # Make sure that the second list or the list of unique hints is global and outside this function. 
                # Let's create an algorithm to select random hints from our list of hints for then user:
                while True:
                    random_select = randint(0,4)    # select a random number from (0,4) , this will be our index range:
                    
                    if open_hint[random_select] in second_list:
                        pass                        # pass through if the the item already exist in our second list
                    elif len(second_list) == 3:
                        break
                    else:
                        second_list.append(open_hint[random_select])
                        continue
                    
            
                hint_label = Label(inner_frame_3 , text = second_list[option-1] , fg = "white" , bg = "paleturquoise" , font = (None , 11))
                hint_label.grid(row = option + 1 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 5)

                option += 1

            except IndexError:
                pass    

    def retry():
        inner_frame_1.grid_forget()
        inner_frame_2.grid_forget()
        inner_frame_3.grid_forget()
        third_bit_hard()

    def quit():
        response_mssg = messagebox.askquestion(None , "Are you sure you want to go back?")
        if str(response_mssg) == "yes":
            inner_frame_1.grid_forget()
            inner_frame_2.grid_forget()
            inner_frame_3.grid_forget()
            second_bit()
        else:
            pass  # just pass by this function if the user doesn't want to quit.


    hint_button = Button(inner_frame_3 , text = "Hint" , command = hint, fg = "white" , bg = "lime" , font = (None , 14) , width = 12 , padx = 10 , pady = 10 , bd = 2 , relief = RAISED)
    hint_button.grid(row = 0 , column = 0 , sticky = W+E , padx = 10 , pady = 10 , columnspan = 3)

    retry_button = Button(inner_frame_3 , text = "Retry" , command = retry, fg = "white" , bg = "gold" , font = (None , 14) , width = 12 , padx = 10 , pady = 10 , bd = 2 , relief = RAISED )
    retry_button.grid(row = option + 6 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)

    quit_button = Button(inner_frame_3 , text = "Leave" , command = quit, fg = "white" , bg = "red" , font = (None , 14) , width = 12 , padx = 10 , pady = 10 , bd = 2 , relief = RAISED )
    quit_button.grid(row = option + 7 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)


def third_bit_easy():
    global frame_2
    global frame_3
    global list_easy
    global tries
    global answer
    global ans_label
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global button_0
    global button_eql
    global button_clear 
    global option
    global unique_list

    # Remove the preious frames
    frame_2.grid_forget()
    frame_3.grid_forget()

    # And adjust the root geometry
    root.geometry("1013x457")
    root.minsize(width = 1013 , height = 457)
    root.maxsize(width = 1013 , height = 457)

    # Let's create our random-number:
    random_number = randrange(100 , 501)
    tries = 1     # The first value for number of tries the user takes
    option = 1    # This is for the hint function, the first hint to be displayed.
    unique_list = [] # Create the unique list or list which holds our unique hints outsise the hint() function
    active_bg_colour = "aquamarine"

    inner_frame_1 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    inner_frame_2 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    inner_frame_3 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    #inner_frame_4 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3 )
    # IMPORTANT point: do not pack()/grid() a widget when it is assigned to a variable.
    # Also don't forget to put LabelFrame to insert a frame inside of a widget.

    inner_frame_1.configure(background = "springgreen")
    inner_frame_2.configure(background = "lightskyblue")
    inner_frame_3.configure(background = "paleturquoise")
    #inner_frame_4.configure(background = "springgreen")

    inner_frame_1.grid(row = 0 , column = 0 , sticky = N+W , padx = 8 , pady = 8)
    inner_frame_2.grid(row = 0 , column = 1 , sticky = N , padx = 8 , pady = 8)
    inner_frame_3.grid(row = 0 , column = 2 , sticky = N+E , padx = 8 , pady = 8)
    #inner_frame_4.grid(row = 1 , column = 0 , sticky = S+W , padx = 8 , pady = 8)

    Label(inner_frame_1 , text = "Info:" , fg = "white" , bg = "springgreen" , font = (None , 14)).grid(row = 0 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
    for item in range(len(list_easy)):
        Label(inner_frame_1 , text = list_easy[item] , fg = "white" , bg = "springgreen" , font = (None , 11)).grid(row = item + 1 , column = 0 , columnspan = 3 ,sticky = W , padx = 5 , pady = 6)

    Label(inner_frame_1 , text = "Number of Tries:" , fg = "white" , bg = "springgreen" , font = (None , 18)).grid(row = 6 , column = 0 , padx = 7 , pady = 15 , sticky = W)

    ans_label = Label(inner_frame_1 , text = "The Answer is :" , fg = "white" , bg = "springgreen" , font = (None , 19))
    ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)

    answer = Label(inner_frame_1 , text = " " , bg = "springgreen" , font = (None , 18))
    answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)

    hints = Label(inner_frame_3 , text = "Hint:" , fg = "white" , bg = "paleturquoise" , font = (None , 11))
    hints.grid(row = 1 , column = 0 , sticky  = W , padx = 10 , pady = 7)

    def choose_hint():
        if random_number % 2 == 0:
            hint_1 = "Number is an Even"
        else:
            hint_1 = "Number is Odd"

        hint_2 = f"Last digit of the number is {random_number % 10}"

        for item in str(random_number):
            hint_3 = f"First digit of the number is {item}"
            break

        mid = int(random_number/2)
        toss = 0
        for item in range(2 , mid+1):
            if random_number % item == 0:
                toss = 1
                break
            else:
                toss = 0
        if toss == 0:
            hint_4 = "It's a prime number"
        else:
            hint_4 = "It's not a prime number" 

        hint_5 = f"It is in the range {random_number - randrange(7,15)} and {random_number + randrange(7,15)}"

        list_of_hints = [hint_1 , hint_2 , hint_3 , hint_4 , hint_5]

        return list_of_hints


    def number_of_tries():
        global tries
        response = Label(inner_frame_1 , text = str(tries) , fg = "white" , bg = "springgreen" , font = (None , 18))
        tries += 1
        response.grid(row = 6 , column = 1 , padx = 7 , pady = 15 , sticky = W)


    entry = Entry(inner_frame_2 , bg = "white" , width = 40)
    entry.grid(row = 0 , column = 0 , columnspan = 3 , sticky = W+E , padx = 3 , pady = 10)

    def select(number):
        current_number = entry.get()       # Here we are trying to store the first number in a temperory variable.
        entry.delete(0 , END)              # Delete everything in the entry block.
        entry.insert(0 , str(current_number) + str(number))

    def equal():
        global answer
        global ans_label
        global button_1
        global button_2
        global button_3
        global button_4
        global button_5
        global button_6
        global button_7
        global button_8
        global button_9
        global button_0
        global button_eql
        global button_clear   
        
        user_number = entry.get()
        entry.delete(0 , END)
        if int(user_number) == random_number:
            ans_label.grid_forget()
            answer.grid_forget()
            button_1.grid_forget()
            button_2.grid_forget()
            button_3.grid_forget()
            button_4.grid_forget()
            button_5.grid_forget()
            button_6.grid_forget()
            button_7.grid_forget()
            button_8.grid_forget()
            button_9.grid_forget()
            button_0.grid_forget()
            button_eql.grid_forget()
            button_clear.grid_forget()

            ans_label = Label(inner_frame_1 , text = "Congratulations.." , fg = "white" , bg = "springgreen" , font = (None , 19))
            ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)

            answer = Label(inner_frame_1 , text = "You Won" , fg = "white" , bg = "springgreen" , font = (None , 19))
            answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
            number_of_tries()

            button_1 = Button(inner_frame_2 , text = "1", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(1) , state = DISABLED)
            button_2 = Button(inner_frame_2 , text = "2", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(2) , state = DISABLED)
            button_3 = Button(inner_frame_2 , text = "3", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(3) , state = DISABLED)
            button_4 = Button(inner_frame_2 , text = "4", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(4) , state = DISABLED)
            button_5 = Button(inner_frame_2 , text = "5", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(5) , state = DISABLED)
            button_6 = Button(inner_frame_2 , text = "6", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(6) , state = DISABLED)
            button_7 = Button(inner_frame_2 , text = "7", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(7) , state = DISABLED)
            button_8 = Button(inner_frame_2 , text = "8", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(8) , state = DISABLED)
            button_9 = Button(inner_frame_2 , text = "9", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(9) , state = DISABLED)
            button_0 = Button(inner_frame_2 , text = "0", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(0) , state = DISABLED)
            button_eql = Button(inner_frame_2 , text = "=" , font = (None , 14) , padx = 90 , pady = 15 , command = lambda:equal() , state = DISABLED)
            button_clear = Button(inner_frame_2 , text = "Clear" , font = (None , 14) , padx = 73 , pady = 15 , command = lambda:clear() , state = DISABLED)

            button_7.grid(row = 1 , column = 0 , padx = 5 , pady = 5)
            button_8.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
            button_9.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

            button_4.grid(row = 2 , column = 0 , padx = 5 , pady = 5)
            button_5.grid(row = 2 , column = 1 , padx = 5 , pady = 5)
            button_6.grid(row = 2 , column = 2 , padx = 5 , pady = 5)

            button_3.grid(row = 3 , column = 0 , padx = 5 , pady = 5)
            button_2.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
            button_1.grid(row = 3 , column = 2 , padx = 5 , pady = 5)
            button_0.grid(row = 4 , column = 0 , padx = 5 , pady = 5)

            button_eql.grid(row = 5 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E)
            button_clear.grid(row = 4 ,column = 1 , columnspan = 2 , padx = 5 , pady = 5)

        elif int(user_number) < 100 or int(user_number) > 500:
                ans_label.grid_forget()
                answer.grid_forget()
                ans_label = Label(inner_frame_1 , text = "Sorry, " , fg = "white" , bg = "springgreen" , font = (None , 19))
                answer = Label(inner_frame_1 , text = "Invalid argument" , fg = "white" , bg = "springgreen" , font = (None , 17))
                ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                
        else:
            if int(user_number) < random_number:
                ans_label.grid_forget()
                answer.grid_forget()
                ans_label = Label(inner_frame_1 , text = "The Answer is :" , fg = "white" , bg = "springgreen" , font = (None , 19))
                answer = Label(inner_frame_1 , text = f"Bigger than {user_number}" , fg = "white" , bg = "springgreen" , font = (None , 18))
                ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                number_of_tries()
            else:
                ans_label.grid_forget()
                answer.grid_forget()
                ans_label = Label(inner_frame_1 , text = "The Answer is :" , fg = "white" , bg = "springgreen" , font = (None , 19))
                answer = Label(inner_frame_1 , text = f"Smaller than {user_number}" , fg = "white" , bg = "springgreen" , font = (None , 18))
                ans_label.grid(row = 7 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 10)
                answer.grid(row = 8 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)
                number_of_tries()


    def clear():
        entry.delete(0 , END)


    button_1 = Button(inner_frame_2 , text = "1", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(1) , activebackground = active_bg_colour)
    button_2 = Button(inner_frame_2 , text = "2", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(2) , activebackground = active_bg_colour)
    button_3 = Button(inner_frame_2 , text = "3", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(3) , activebackground = active_bg_colour)
    button_4 = Button(inner_frame_2 , text = "4", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(4) , activebackground = active_bg_colour)
    button_5 = Button(inner_frame_2 , text = "5", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(5) , activebackground = active_bg_colour)
    button_6 = Button(inner_frame_2 , text = "6", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(6) , activebackground = active_bg_colour)
    button_7 = Button(inner_frame_2 , text = "7", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(7) , activebackground = active_bg_colour)
    button_8 = Button(inner_frame_2 , text = "8", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(8) , activebackground = active_bg_colour)
    button_9 = Button(inner_frame_2 , text = "9", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(9) , activebackground = active_bg_colour)
    button_0 = Button(inner_frame_2 , text = "0", font = (None , 14) , padx = 35 , pady = 15 , command = lambda:select(0) , activebackground = active_bg_colour)
    button_eql = Button(inner_frame_2 , text = "=" , font = (None , 14) , padx = 90 , pady = 15 , command = lambda:equal() , activebackground = active_bg_colour)
    button_clear = Button(inner_frame_2 , text = "Clear" , font = (None , 14) , padx = 73 , pady = 15 , command = lambda:clear() , activebackground = active_bg_colour)

    button_7.grid(row = 1 , column = 0 , padx = 5 , pady = 5)
    button_8.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
    button_9.grid(row = 1 , column = 2 , padx = 5 , pady = 5)

    button_4.grid(row = 2 , column = 0 , padx = 5 , pady = 5)
    button_5.grid(row = 2 , column = 1 , padx = 5 , pady = 5)
    button_6.grid(row = 2 , column = 2 , padx = 5 , pady = 5)

    button_3.grid(row = 3 , column = 0 , padx = 5 , pady = 5)
    button_2.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
    button_1.grid(row = 3 , column = 2 , padx = 5 , pady = 5)
    button_0.grid(row = 4 , column = 0 , padx = 5 , pady = 5)

    button_eql.grid(row = 5 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E)
    button_clear.grid(row = 4 ,column = 1 , columnspan = 2 , padx = 5 , pady = 5)


    def hint():
        #while True: <-- do not use while here as it will crash the program
            try:
                global option
                global unique_list
                open_hint = choose_hint()
                # Let's again create our algorithm to produce unique hints for our user:
                while True:
                    random_select = randint(0,4)

                    if len(unique_list) == 5:
                        break

                    if open_hint[random_select] in unique_list:
                        pass

                    else:
                        unique_list.append(open_hint[random_select])
                        continue

                    
                ''' Use this if you want the hints to be in order:
                second_list = []
                for item in open_hint:
                    if item in second_list:
                        continue
                    else:
                        second_list.append(item)
                '''
            
                hint_label = Label(inner_frame_3 , text = unique_list[option-1] , fg = "white" , bg = "paleturquoise" , font = (None , 11))
                hint_label.grid(row = option + 1 , column = 0 , columnspan = 3 , sticky = W , padx = 10 , pady = 5)

                option += 1

            except IndexError:
                pass    

    def retry():
        inner_frame_1.grid_forget()
        inner_frame_2.grid_forget()
        inner_frame_3.grid_forget()
        third_bit_easy()

    def quit():
        response_mssg = messagebox.askquestion(None , "Are you sure you want to go back?")
        if str(response_mssg) == "yes":
            inner_frame_1.grid_forget()
            inner_frame_2.grid_forget()
            inner_frame_3.grid_forget()
            second_bit()
        else:
            pass  # just pass by this function if the user doesn't want to quit.


    hint_button = Button(inner_frame_3 , text = "Hint" , command = hint, fg = "white" , bg = "lime" , font = (None , 14) , width = 12 , padx = 10 , pady = 10 , bd = 2 , relief = RAISED)
    hint_button.grid(row = 0 , column = 0 , sticky = W+E , padx = 10 , pady = 10 , columnspan = 3)

    retry_button = Button(inner_frame_3 , text = "Retry" , command = retry, fg = "white" , bg = "gold" , font = (None , 14) , width = 12 , padx = 10 , pady = 10 , bd = 2 , relief = RAISED )
    retry_button.grid(row = option + 6 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)

    quit_button = Button(inner_frame_3 , text = "Leave" , command = quit, fg = "white" , bg = "red" , font = (None , 14) , width = 12 , padx = 10 , pady = 10 , bd = 2 , relief = RAISED )
    quit_button.grid(row = option + 7 , column = 0 , columnspan = 3 , sticky = W+E , padx = 10 , pady = 10)


    #Button(root , text = "1" , command = third_bit_easy).grid(row = 0 , column = 0 , sticky = S+W)


def second_bit():
    global frame_2
    global frame_3
    global list_easy
    global list_hard

    root.geometry("950x400")
    root.minsize(width = 950 , height = 400)
    root.maxsize(width = 950 , height = 400)

    frame_2 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    frame_3 = LabelFrame(root , text = "" , padx = 3 , pady = 3 , bd = 3)
    frame_2.configure(background = "light blue")
    frame_3.configure(background = "light blue")
    frame_2.grid(row = 0 , column = 0 , sticky = W , padx = 10 , pady = 10)
    frame_3.grid(row = 0 , column = 1 , sticky = E , padx = 10 , pady = 10)

    Label(frame_2 , text = "Difficulty : EASY" , fg = "white" , bg = "springgreen" , font = (None , 18) , relief = RAISED).grid(row = 0 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E) 
    Label(frame_3 , text = "Difficulty : HARD" , fg = "white" , bg = "red" , font = (None , 18) , relief = RAISED).grid(row = 0 , column = 0 , columnspan = 3 , padx = 5 , pady = 5 , sticky = W+E )

    Label(frame_2 , text = "Info:" , fg = 'white' , bg = "light blue" , font = (None , 14)).grid(row = 1 ,  column = 0 , columnspan = 3 , sticky = W , padx = 5 , pady = 5)
    Label(frame_3 , text = "Info:" , fg = 'white' , bg = "light blue" , font = (None , 14)).grid(row = 1 ,  column = 0 , columnspan = 3 , sticky = W , padx = 5 , pady = 5)

    list_easy = [
        "1.Guess a number between 100 and 500" ,
        "2.You can take as many guesses as you wish." , 
        "3.'HINT' button will be given and can be used up to 5 times." , 
        "4.You can Leave the game at anytime you want."
    ]

    list_hard = [
        "1.Guess a number between 0 and 500" ,
        "2.You have a limited number of guesses." , 
        "3.'HINT' button will be given and can be used up to 3 times." , 
        "4.You can Leave the game at anytime you want."
    ]   

    for item in range(len(list_easy)):
        Label(frame_2 , text = list_easy[item] , fg = "white" , bg = "light blue" , font = (None , 13)).grid(row = item + 2 , column = 0 , columnspan = 3 , sticky = W , padx = 5 , pady = 4)

    for item in range(len(list_easy)):
        Label(frame_3 , text = list_hard[item] , fg = "white" , bg = "light blue" , font = (None , 13)).grid(row = item + 2 , column = 0 , columnspan = 3 , sticky = W , padx = 5 , pady = 4)

    Label(frame_2 , text = "Are you ready?" , fg = "white" , bg = "light blue" , font = (None , 15)).grid(row = 6 , column = 0 , columnspan = 3 , sticky = W+E , padx = 5 , pady = 6)
    Label(frame_3 , text = "Are you ready?" , fg = "white" , bg = "light blue" , font = (None , 15)).grid(row = 6 , column = 0 , columnspan = 3 , sticky = W+E , padx = 5 , pady = 6)

    def exit_program():
        response = messagebox.askquestion(None , "Are you sure you want to QUIT?")
        if str(response) == "yes":
            root.destroy()
        else:
            frame_2.grid_forget()
            frame_3.grid_forget()
            second_bit()

    Button(frame_2 , text = "Start the Game" , command = third_bit_easy , fg = "white" , bg = "mediumspringgreen" , width = 12 , padx = 20 , pady = 20 , font = (None , 13) , bd = 3).grid(row = 7 , column = 0 , sticky = W , padx = 5 , pady = 10)
    Button(frame_2 , text = "Exit" , command = exit_program , fg = "white" , bg = "red" , width = 12 , padx = 20 , pady = 20 , font = (None , 13) , bd = 3).grid(row = 7 , column = 2 , sticky = E , padx = 5 , pady = 10)

    Button(frame_3 , text = "Start the Game" , command = third_bit_hard, fg = "white" , bg = "mediumspringgreen" , width = 12 , padx = 20 , pady = 20 , font = (None , 13) , bd = 3).grid(row = 7 , column = 0 , sticky = W , padx = 5 , pady = 10)
    Button(frame_3 , text = "Exit" , command = exit_program, fg = "white" , bg = "red" , width = 12 , padx = 20 , pady = 20 , font = (None , 13) , bd = 3).grid(row = 7 , column = 2 , sticky = E , padx = 5 , pady = 10)


def first_bit():
    global frame
    global button_start
    global button_exit
    
    # Set the Max and Min sizes for your widget
    root.minsize(width = 660 , height = 480)
    root.maxsize(width = 660 , height = 480)


    frame = LabelFrame(root ,text = "", padx = 3 , pady = 3 , bd = 3)
    frame.configure(background = "light blue")
    frame.grid(row = 0 , column = 1 , sticky = W+E , padx = 10 , pady = 10)
    #frame.place(anchor = CENTER)

    Label(frame , text = " Welcome to my Guessing game" , fg = "snow", bg = "light blue" , font = (None , 19)).grid(row = 0 , column = 0 , columnspan = 3,  padx = 5 , sticky = W+E)
    Label(frame , text = "* INSTRUCTIONS *" , fg = "white", bg = "lightpink" , font = (None , 15) , bd = 3 , relief = RAISED).grid(row = 1 , column = 0 , columnspan = 1, padx = 5 , pady = 10)

    lst = [
        "Select the Difficulty , Easy or Hard",
        "Guess the number selected by the program",
        "If you're stuck or can't figure out the answer , Press the 'Hint' button",
        "Wanna play again? Press the 'Retry' button",
        "You can leave the game at any moment by pressing the 'Leave' button"
    ]

    for string in range(len(lst)):
        rules = Radiobutton(frame , text = lst[string] , fg = "white", bg = "light blue" , font = (None , 14) , activebackground = "lightblue" , activeforeground = "white" , state = NORMAL , selectcolor = "white")
        rules.grid(row = string + 2 , column = 0 , columnspan = 1, padx = 5 , pady = 10 , sticky = W)

        # Use sticky to stick the strings onto one side, acts like an anchor in grid.

    def start_program():
        global frame
        global button_exit
        global button_start

        frame.grid_forget()
        button_exit.grid_forget()
        button_start.grid_forget()
        #root.geometry("950x400")
        second_bit()

    def exit_program():
        #global root
        response = messagebox.askquestion(None , "Are you sure you want to QUIT?")
        if str(response) == "yes":
            root.destroy()
        else:
            frame.grid_forget()
            button_exit.grid_forget()
            button_start.grid_forget()
            first_bit()


    button_start = Button(root , text = "START" , command = start_program , fg = "white" , bg = "springgreen" , bd = 3 , padx = 20 , pady = 20 , width = 18 , height = 1, font = (None , 13))
    button_exit = Button(root , text = "EXIT" , command = exit_program , fg = "white" , bg = "red" , bd = 3 , padx = 20 , pady = 20 , width = 18,  height = 1, font = (None , 13))

    button_start.grid(row = 1 , column = 1 , padx = 10 , pady = 10 , sticky = W)
    button_exit.grid(row = 1 , column = 1, padx = 10 , pady = 10 , sticky = E)

first_bit()


root.mainloop()