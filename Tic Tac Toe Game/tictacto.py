# import everything from tkinter
from tkinter import *

# For the buttons
from tkinter import ttk

# for displaying messages
from tkinter import messagebox


def checkWinner():
    if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
            button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
            button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
            button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
            button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
            button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
            button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
            button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        messagebox._show("Winner ", "Player O is the winner")


    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
          button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        messagebox._show("Winner ", "Player X is the winner")


# root Window
root = Tk()

# display the window size
root.geometry("530x370")

# defining the buttons
button1 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(1))
button1.grid(row=0, column=0, ipadx=50, ipady=50)

button2 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(2))
button2.grid(row=0, column=1, ipadx=50, ipady=50)

button3 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(3))
button3.grid(row=0, column=2, ipadx=50, ipady=50)

button4 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(4))
button4.grid(row=1, column=0, ipadx=50, ipady=50)

button5 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(5))
button5.grid(row=1, column=1, ipadx=50, ipady=50)

button6 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(6))
button6.grid(row=1, column=2, ipadx=50, ipady=50)

button7 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(7))
button7.grid(row=2, column=0, ipadx=50, ipady=50)

button8 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(8))
button8.grid(row=2, column=1, ipadx=50, ipady=50)

button9 = ttk.Button(root, text=' ', command=lambda: ButtonPressed(9))
button9.grid(row=2, column=2, ipadx=50, ipady=50)

player = 1


def ButtonPressed(ButtonNumber):
    global player

    # Button1
    if ButtonNumber == 1 and player == 1:
        button1.config(text='X')
        player = 2
    elif ButtonNumber == 1 and player == 2:
        button1.config(text='O')
        player = 1

    # Button2
    elif ButtonNumber == 2 and player == 1:
        button2.config(text='X')
        player = 2
    elif ButtonNumber == 2 and player == 2:
        button2.config(text='O')
        player = 1

    # Button3
    elif ButtonNumber == 3 and player == 1:
        button3.config(text='X')
        player = 2
    elif ButtonNumber == 3 and player == 2:
        button3.config(text='O')
        player = 1

    # Button4
    elif ButtonNumber == 4 and player == 1:
        button4.config(text='X')
        player = 2
    elif ButtonNumber == 4 and player == 2:
        button4.config(text='O')
        player = 1

    # Button5
    elif ButtonNumber == 5 and player == 1:
        button5.config(text='X')
        player = 2
    elif ButtonNumber == 5 and player == 2:
        button5.config(text='O')
        player = 1

    # Button6
    elif ButtonNumber == 6 and player == 1:
        button6.config(text='X')
        player = 2
    elif ButtonNumber == 6 and player == 2:
        button6.config(text='O')
        player = 1

    # Button7
    elif ButtonNumber == 7 and player == 1:
        button7.config(text='X')
        player = 2
    elif ButtonNumber == 7 and player == 2:
        button7.config(text='O')
        player = 1

    # Button8
    elif ButtonNumber == 8 and player == 1:
        button8.config(text='X')
        player = 2
    elif ButtonNumber == 8 and player == 2:
        button8.config(text='O')
        player = 1

    # Button9
    elif ButtonNumber == 9 and player == 1:
        button9.config(text='X')
        player = 2
    elif ButtonNumber == 9 and player == 2:
        button9.config(text='O')
        player = 1

    checkWinner()




root.mainloop()
