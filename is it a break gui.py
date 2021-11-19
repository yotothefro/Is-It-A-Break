from tkinter import *
import pygame
import pyglet
import random

#main window setup
root = Tk()
root.title("BREAK TIME")
root.geometry("500x500")
root.state("zoomed")

#background image
bg = PhotoImage(file="/Users/theop/OneDrive/Desktop/break time addons/dudes.png")
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# text = PhotoImage(file="C:/Users/theop/OneDrive/Desktop/break time addons/Removal-411.png")
# my_label2 = Label(root, image=text)
# my_label2.pack()

#background music
pygame.mixer.init()

def play():
    pygame.mixer.music.load("C:/Users/theop/OneDrive/Desktop/break time addons/Enemy (from the series Arcane League of Legends).mp3")
    pygame.mixer.music.play()

play()

#font import + break time motherfucker text
pyglet.font.add_file("C:/Users/theop/OneDrive/Desktop/break time addons/Friz-Quadrata-Font/Friz Quadrata Regular.ttf")
lolLabel = Label(root,text="BREAK TIME MOTHERFUCKER",font=('Friz Quadrata',50), bg="black", fg="white")
lolLabel.pack(pady=10)

#buttons to answer, need to add command
yesbtn = Button(text="YES", bg="black", width=23, fg="white", font=('Friz Quadrata',20))
yesbtn.place(x=400, y=850)
isbtn = Button(text="IS IT A BREAK?", bg="black", width=23, fg="white", font=('Friz Quadrata',20))
isbtn.place(x=800, y=850)
downbtn = Button(text="YOU DOWN FOR A BREAK?", bg="black", width=23, fg="white", font=('Friz Quadrata',20))
downbtn.place(x=1200, y=850)
   
#text display for answer
texts = ["YOU DOWN FOR A BREAK?", "IS IT A BREAK?", "YES"]
# yes = texts[2]
# isit = texts[1]
# down = [0]
# for n in range(0, 3):
#     n = random.randint(0, 3)
    
n = random.randint(0, 3)
item = texts[n]
answer = Label(root, text=item, font=('Friz Quadrata',40), bg="black", fg="white")
answer.place(x=800, y=700)

    

#timer





root.mainloop()