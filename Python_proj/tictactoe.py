# Tic-tac-toe
from tkinter import *
from tkinter import messagebox

def main():
        
    global player_1
    global player_2

    global player_1_point
    global player_2_point

    global inner_frame
    global score_label
    global score_label_2

    root = Tk()
    root.title("tic-tac-toe")
    root.iconbitmap("visual_studio_code_icon_191771.ico")

    player_1 = True   # blue
    player_2 = False  # red

    player_1_point = 0
    player_2_point = 0

    def player_enter(event):

        if player_1 == True and player_2 == False:
            #event.widget.tk_focusFollowsMouse()    <- if you want to focus the widget when the mouse is inside of it
            if event.widget.cget("bg") == "lightblue" or event.widget.cget("bg") == "pink":  # .cget() is use to get the value of specified option.
                pass
            else:
                event.widget.config(bg = "blue")

        elif player_1 == False and player_2 == True:
            #event.widget.tk_focusFollowsMouse()
            if event.widget.cget("bg") == "lightblue" or event.widget.cget("bg") == "pink":
                pass
            else:
                event.widget.config(bg = "red")

    def player_leave(event):

        if player_1 == True and player_2 == False:
            if event.widget.cget("bg") == "lightblue" or event.widget.cget("bg") == "pink":
                pass
            else:
                event.widget.config(bg = "snow")

        elif player_1 == False and player_2 == True:
            if event.widget.cget("bg") == "lightblue" or event.widget.cget("bg") == "pink":
                pass
            else:
                event.widget.config(bg = "snow")

    def defocus(event):
        event.widget.master.focus_set()

    def retry_fun():

        global player_1
        global player_2

        player_1 = True
        player_2 = False

        button_1.config(bg = "snow")
        button_2.config(bg = "snow")
        button_3.config(bg = "snow")
        button_4.config(bg = "snow")
        button_5.config(bg = "snow")
        button_6.config(bg = "snow")
        button_7.config(bg = "snow")
        button_8.config(bg = "snow")
        button_9.config(bg = "snow")

        button_1.bind("<Button-1>" , select_this)
        button_2.bind("<Button-1>" , select_this)
        button_3.bind("<Button-1>" , select_this)
        button_4.bind("<Button-1>" , select_this)
        button_5.bind("<Button-1>" , select_this)
        button_6.bind("<Button-1>" , select_this)
        button_7.bind("<Button-1>" , select_this)
        button_8.bind("<Button-1>" , select_this)
        button_9.bind("<Button-1>" , select_this)

        button_1.bind("<Enter>" , player_enter)
        button_2.bind("<Enter>" , player_enter)
        button_3.bind("<Enter>" , player_enter)
        button_4.bind("<Enter>" , player_enter)
        button_5.bind("<Enter>" , player_enter)
        button_6.bind("<Enter>" , player_enter)
        button_7.bind("<Enter>" , player_enter)
        button_8.bind("<Enter>" , player_enter)
        button_9.bind("<Enter>" , player_enter)

        button_1.bind("<Leave>" , player_leave)
        button_2.bind("<Leave>" , player_leave)
        button_3.bind("<Leave>" , player_leave)
        button_4.bind("<Leave>" , player_leave)
        button_5.bind("<Leave>" , player_leave)
        button_6.bind("<Leave>" , player_leave)
        button_7.bind("<Leave>" , player_leave)
        button_8.bind("<Leave>" , player_leave)
        button_9.bind("<Leave>" , player_leave)

    def exit_fun():
        root.destroy()

    def disable_widgets():

        button_1.config(state = DISABLED)
        button_2.config(state = DISABLED)
        button_3.config(state = DISABLED)
        button_4.config(state = DISABLED)
        button_5.config(state = DISABLED)
        button_6.config(state = DISABLED)
        button_7.config(state = DISABLED)
        button_8.config(state = DISABLED)
        button_9.config(state = DISABLED)

        button_1.unbind("<Button-1>")
        button_2.unbind("<Button-1>")
        button_3.unbind("<Button-1>")
        button_4.unbind("<Button-1>")
        button_5.unbind("<Button-1>")
        button_6.unbind("<Button-1>")
        button_7.unbind("<Button-1>")
        button_8.unbind("<Button-1>")
        button_9.unbind("<Button-1>")

        button_1.unbind("<Enter>")
        button_2.unbind("<Enter>")
        button_3.unbind("<Enter>")
        button_4.unbind("<Enter>")
        button_5.unbind("<Enter>")
        button_6.unbind("<Enter>")
        button_7.unbind("<Enter>")
        button_8.unbind("<Enter>")
        button_9.unbind("<Enter>")

        button_1.unbind("<Leave>")
        button_2.unbind("<Leave>")
        button_3.unbind("<Leave>")
        button_4.unbind("<Leave>")
        button_5.unbind("<Leave>")
        button_6.unbind("<Leave>")
        button_7.unbind("<Leave>")
        button_8.unbind("<Leave>")
        button_9.unbind("<Leave>")

    def reset_points():

        global player_1_point
        global player_2_point

        global player_1
        global player_2

        global score_label
        global score_label_2

        #global message

        message = messagebox.askyesnocancel(title = "Reset Message" , message = "Do You Want To Reset Your Game Progress as Well?\nUpon Clicking 'Yes' Your Entire Progress And Score Will Be Re-Initialized.")
        if message == True:
            
            retry_fun()

            player_1_point = 0
            player_2_point = 0

            score_label.grid_forget()
            score_label_2.grid_forget()

            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)

            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)

        elif message == False:

            player_1_point = 0
            player_2_point = 0

            score_label.grid_forget()
            score_label_2.grid_forget()

            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)

            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)

        else:
            pass

    def check_win():

        global set_score_frame
        global inner_frame

        global player_1_point
        global player_2_point

        global score_label
        global score_label_2

        top_left = button_1.cget("bg")
        top_mid = button_2.cget("bg")
        top_right = button_3.cget("bg")

        mid_left = button_4.cget("bg")
        mid_mid = button_5.cget("bg")
        mid_right = button_6.cget("bg")

        bottom_left = button_7.cget("bg")
        bottom_mid = button_8.cget("bg")
        bottom_right = button_9.cget("bg")


        if top_left == "lightblue" and top_mid == "lightblue" and top_right == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_1.config(bg = "springgreen")
            button_2.config(bg = "springgreen")
            button_3.config(bg = "springgreen")
            disable_widgets()
            
        elif mid_left == "lightblue" and mid_mid == "lightblue" and mid_right == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_4.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_6.config(bg = "springgreen")
            disable_widgets()

        elif bottom_left == "lightblue" and bottom_mid == "lightblue" and bottom_right == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_7.config(bg = "springgreen")
            button_8.config(bg = "springgreen")
            button_9.config(bg = "springgreen")
            disable_widgets()

        elif top_left == "lightblue" and mid_left == "lightblue" and bottom_left == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_1.config(bg = "springgreen")
            button_4.config(bg = "springgreen")
            button_7.config(bg = "springgreen")
            disable_widgets()

        elif top_mid == "lightblue" and mid_mid == "lightblue" and bottom_mid == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_2.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_8.config(bg = "springgreen")
            disable_widgets()

        elif top_right == "lightblue" and mid_right == "lightblue" and bottom_right == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_3.config(bg = "springgreen")
            button_6.config(bg = "springgreen")
            button_9.config(bg = "springgreen") 
            disable_widgets()

        elif top_left == "lightblue" and mid_mid == "lightblue" and bottom_right == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_1.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_9.config(bg = "springgreen")
            disable_widgets()

        elif top_right == "lightblue" and mid_mid == "lightblue" and bottom_left == "lightblue":
            player_1_point += 1
            score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)
            button_3.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_7.config(bg = "springgreen")
            disable_widgets()

        elif top_left == "pink" and top_mid == "pink" and top_right == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_1.config(bg = "springgreen")
            button_2.config(bg = "springgreen")
            button_3.config(bg = "springgreen")
            disable_widgets()
            
        elif mid_left == "pink" and mid_mid == "pink" and mid_right == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_4.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_6.config(bg = "springgreen")
            disable_widgets()

        elif bottom_left == "pink" and bottom_mid == "pink" and bottom_right == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_7.config(bg = "springgreen")
            button_8.config(bg = "springgreen")
            button_9.config(bg = "springgreen")
            disable_widgets()

        elif top_left == "pink" and mid_left == "pink" and bottom_left == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_1.config(bg = "springgreen")
            button_4.config(bg = "springgreen")
            button_7.config(bg = "springgreen")
            disable_widgets()

        elif top_mid == "pink" and mid_mid == "pink" and bottom_mid == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_2.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_8.config(bg = "springgreen")
            disable_widgets()

        elif top_right == "pink" and mid_right == "pink" and bottom_right == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_3.config(bg = "springgreen")
            button_6.config(bg = "springgreen")
            button_9.config(bg = "springgreen")
            disable_widgets()

        elif top_left == "pink" and mid_mid == "pink" and bottom_right == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_1.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_9.config(bg = "springgreen")
            disable_widgets()

        elif top_right == "pink" and mid_mid == "pink" and bottom_left == "pink":
            player_2_point += 1
            score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
            score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)
            button_3.config(bg = "springgreen")
            button_5.config(bg = "springgreen")
            button_7.config(bg = "springgreen")
            disable_widgets()


    def select_this(event):
        global player_1 
        global player_2

        if player_1 == True and player_2 == False:
            if event.widget.cget("bg") == "lightblue" or event.widget.cget("bg") == "pink":
                pass
            else:
                event.widget.config(bg = "lightblue")
                check_win()
                player_1 = False 
                player_2 = True

        elif player_1 == False and player_2 == True:
            if event.widget.cget("bg") == "lightblue" or event.widget.cget("bg") == "pink":
                pass
            else:
                event.widget.config(bg = "pink")
                check_win()
                player_1 = True
                player_2 = False

    name_label = Label(root , text = "tic-tac-toe" , font = "Helvetica 15 bold" , anchor = E , bg = "grey")
    name_label.grid(row = 0 , column = 0 , columnspan = 3 , sticky = W + E)

    set_score_frame = Frame(root , bg = "black")
    set_score_frame.grid(row = 4 , column = 0 , columnspan = 3 , sticky = W + E , pady = (5 , 0))

    inner_frame = Frame(set_score_frame , bg = "slategrey")
    inner_frame.grid(row = 0 , column = 0 , padx = 1 , pady = 1 , sticky = NSEW )

    player_1_info = Label(inner_frame , text = "Player 1:" , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "white")
    player_2_info = Label(inner_frame , text = "Player 2:" , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "white")

    player_1_info.grid(row = 0 , column = 0 , sticky = W , padx = (10,0) , pady = 5)
    player_2_info.grid(row = 1 , column = 0 , sticky = W , padx = (10,0) , pady = 5)

    player_1_colour = Entry(inner_frame , bg = "blue" , width = 3 , bd = 0 , cursor = "arrow snow")
    player_1_colour.bind("<FocusIn>" , defocus)
    player_1_colour.grid(row = 0 , column = 1 , padx = 2 , pady = 5 , sticky = E)

    player_2_colour = Entry(inner_frame , bg = "red" , width = 3 , bd = 0 , cursor = "arrow snow")
    player_2_colour.bind("<FocusIn>" , defocus)
    player_2_colour.grid(row = 1 , column = 1 , padx = 2 , pady = 5 , sticky = E)

    retry_button = Button(inner_frame , text = "Retry" , font = "Helvetica 12 bold" , bg = "mediumspringgreen" , fg = "snow" , command = retry_fun , underline = 0)
    retry_button.grid(row = 0 , rowspan = 2 , column = 3 , pady = 7 , padx = (95 , 15) , ipadx = 25 , ipady = 2 )

    exit_button = Button(inner_frame , text = "Exit" , font = "Helvetica 12 bold" , bg = "red" , fg = "snow" , command = exit_fun , underline = 0)
    exit_button.grid(row = 0 , column = 4 , rowspan = 2 , pady = 7 , padx = (60 , 30) , ipadx = 25 , ipady = 2 , sticky = E)

    score = Label(inner_frame , text = "-Score-" , font = "Helvetica 12 bold italic" , bg = "darkslategrey" , fg = "white")
    score.grid(row = 2 , column = 0 , columnspan = 5 ,padx = (10 , 10) , pady = (10 , 5) , sticky = W + E)

    Label(inner_frame , text = "Player 1:" , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow" , underline = 0).grid(row = 3 , column = 3 ,padx = (5 , 0), pady = (5 , 10) , sticky = W)

    Label(inner_frame , text = "Player 2:" , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow" , underline = 0).grid(row = 3 , column = 4 , pady = (5 , 10) , sticky = W)

    reset_button = Button(inner_frame , text = "Reset" , font = "Helvetica 12 bold" , bg = "skyblue" , fg = "snow" , command = reset_points)
    reset_button.grid(row = 3 , column = 0 , padx = (10 , 0) , pady = (5 , 10) , sticky = N , ipadx = 10 , ipady = 0)

    score_label = Label(inner_frame , text = str(player_1_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
    score_label.grid(row = 3 , column = 3 , padx = (0 , 0) , pady = (5 , 11) , sticky = NS)

    score_label_2 = Label(inner_frame , text = str(player_2_point) , font = "Helvetica 12 bold" , bg = "slategrey" , fg = "snow")
    score_label_2.grid(row = 3 , column = 4 , padx = (8, 0) , pady = (5 , 11) , sticky = NS)

    # Create 9 Buttons:
    button_1 = Button(root , bd = 0 , bg = "snow")
    button_2 = Button(root , bd = 0 , bg = "snow")
    button_3 = Button(root , bd = 0 , bg = "snow")
    button_4 = Button(root , bd = 0 , bg = "snow")
    button_5 = Button(root , bd = 0 , bg = "snow")
    button_6 = Button(root , bd = 0 , bg = "snow")
    button_7 = Button(root , bd = 0 , bg = "snow")
    button_8 = Button(root , bd = 0 , bg = "snow")
    button_9 = Button(root , bd = 0 , bg = "snow")

    # binding of buttons:
    button_1.bind("<Button-1>" , select_this)
    button_2.bind("<Button-1>" , select_this)
    button_3.bind("<Button-1>" , select_this)
    button_4.bind("<Button-1>" , select_this)
    button_5.bind("<Button-1>" , select_this)
    button_6.bind("<Button-1>" , select_this)
    button_7.bind("<Button-1>" , select_this)
    button_8.bind("<Button-1>" , select_this)
    button_9.bind("<Button-1>" , select_this)

    button_1.bind("<Enter>" , player_enter)
    button_2.bind("<Enter>" , player_enter)
    button_3.bind("<Enter>" , player_enter)
    button_4.bind("<Enter>" , player_enter)
    button_5.bind("<Enter>" , player_enter)
    button_6.bind("<Enter>" , player_enter)
    button_7.bind("<Enter>" , player_enter)
    button_8.bind("<Enter>" , player_enter)
    button_9.bind("<Enter>" , player_enter)

    button_1.bind("<Leave>" , player_leave)
    button_2.bind("<Leave>" , player_leave)
    button_3.bind("<Leave>" , player_leave)
    button_4.bind("<Leave>" , player_leave)
    button_5.bind("<Leave>" , player_leave)
    button_6.bind("<Leave>" , player_leave)
    button_7.bind("<Leave>" , player_leave)
    button_8.bind("<Leave>" , player_leave)
    button_9.bind("<Leave>" , player_leave)

    # Grid them on the screen
    button_1.grid(row =1 , column = 0 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_2.grid(row =1 , column = 1 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_3.grid(row =1 , column = 2 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_4.grid(row =2 , column = 0 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_5.grid(row =2 , column = 1 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_6.grid(row =2 , column = 2 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_7.grid(row =3 , column = 0 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_8.grid(row =3 , column = 1 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)
    button_9.grid(row =3 , column = 2 , ipadx = 80 , ipady = 60 , padx = 1 , pady = 2)


    '''
    root.columnconfigure(0 , weight = 1)
    root.columnconfigure(2 , weight = 1)


    root.rowconfigure(1 , weight = 1)
    root.rowconfigure(2 , weight = 1)
    '''
    root.mainloop()

if __name__ == "__main__":      # By specifing an idiome your turning this file into an python script
    main()