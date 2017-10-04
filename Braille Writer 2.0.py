from tkinter import *
master = Tk()
master.title("Braille")
x=0
y=0
circlex=5
circley=5
changex = 7
changey = 7
letters={"a":[1,0,0,0,0,0],
         "b":[1,0,1,0,0,0],
         "c":[1,1,0,0,0,0],
         "d":[1,1,0,1,0,0],
         "e":[1,0,0,1,0,0],
         "f":[1,1,1,0,0,0],
         "g":[1,1,1,1,0,0],
         "h":[1,0,1,1,0,0],
         "i":[0,1,1,0,0,0],
         "j":[0,1,1,1,0,0],
         "k":[1,0,0,0,1,0],
         "l":[1,0,1,0,1,0],
         "m":[1,1,0,0,1,0],
         "n":[1,1,0,1,1,0],
         "o":[1,0,0,1,1,0],
         "p":[1,1,1,0,1,0],
         "q":[1,1,1,1,1,0],
         "r":[1,0,1,1,1,0],
         "s":[0,1,1,0,1,0],
         "t":[0,1,1,1,1,0],
         "u":[1,0,0,0,1,1],
         "v":[1,0,1,0,1,1],
         "w":[0,1,1,1,0,1],
         "x":[1,1,0,0,1,1],
         "y":[1,1,0,1,1,1],
         "z":[1,0,0,1,1,1],
         " ":[0,0,0,0,0,0],
         "!":[0,0,1,1,1,0],
         "'":[0,0,0,0,1,0],
         ",":[0,0,1,0,0,0],
         "_":[0,0,0,0,1,1],
         ".":[0,0,1,1,0,1],
         "?":[0,0,1,0,1,1]}

def convert(event):
    global letters
    global changex
    global changey
    count=0
    for x in letters[event.char.lower()]:
        if x == 1:
            canvas.itemconfig(canvas.find_overlapping(changex,changey,changex,changey),fill="black")
        if count == 0:
            changex+= 7
            count+=1
        else:
            changex-=7
            changey+=7
            count = 0
        
    changey -= 21
    changex += 17
    if changex == 500:
        changex = 7
        changey +=24
        
    
canvas = Canvas(master, width=500, height=500)
canvas.grid(row=0,column=0)
canvas.focus_set()
for x in range(58*60):
    if x != 0:
        canvas.create_oval(circlex,circley,circlex+5,circley+5,fill="white")
        if (x) % 2 == 0:
            circlex += 10
        else:
            circlex+=7
            
        if x % 174 == 0:
            circley += 10
            circlex = 5
        elif x % 58 == 0:
            circley += 7
            circlex = 5
            
canvas.create_oval(circlex,circley,circlex+5,circley+5,fill="white")
canvas.bind("<Key>",convert)


while True:
    master.update()
