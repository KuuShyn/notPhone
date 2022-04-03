#King Aj Magalona - SOLO


# import Button
from tkinter import BOTTOM, TOP, Entry, Label, StringVar, Tk, Button, RAISED

text = ""

root = Tk()
root.resizable(False, False)

empty = Label(root)
empty.grid(row=0,column=0)  # Just to RePosition the Grid hehe

num = StringVar()
textbox = Entry(root, textvariable=num, state='readonly') 
textbox.place(x=1, y=1, width=110)


labels = [['1', '2', '3'],  # phone dial label texts
          ['4', '5', '6'],  # organized in a grid
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):  # for every row r = 0, 1, 2, 3
    for c in range(3):  # for every row c = 0, 1, 2
        # create label for row r and column c

        # A separate handler function must be defined for each button.
        # They are effectively the same function but with different default inputs.
        def handler(x=labels[r][c]):
            global text
            text = text +str(x)
            num.set(text)      

        # button instead of label
        buttons = Button(root,
                        relief=RAISED,  # raised border
                        padx=10,  # make label wide 
                        text=labels[r][c],
                        command=handler, )  # label text
        # place label in row r and column c
        buttons.grid(row=r+1, column=c)


def clear():    
    global text
    text = ""
    num.set("")

btnClear = Button(root, relief=RAISED, text="clear", command= clear)
btnClear.grid(row=5, column=1)

root.mainloop()
