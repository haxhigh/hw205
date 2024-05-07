import socket
from tkinter import *
from threading import Thread
import random
import tkinter
from PIL import ImageTk, Image
import platform

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT 

    PORT = 5000
    IP_ADDRESS = "127.0.0.1"
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    SERVER.connect((IP_ADDRESS,PORT))

    thread = Thread(target=recivedMsg)
    thread.start()
    askPlayerName()

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    
    nameWindow = Tk()
    nameWindow.title("tumbola game!")
    nameWindow.geometry("500x500")

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw\Hw204/assets/background.png")

    canvas1 = Canvas(nameWindow,width = 500,height = 500)
    canvas1.create_image(0,0,bg=bg,anchor = "nw")

    canvas1.create_text(screen_width/4.5,screen_height/8,text="Enter your name!")
    
    nameEntry = Entry(nameWindow,width=5,justify="center")
    nameEntry.place(screen_width/7,screen_height/5.5)

    saveButton = Button(nameWindow,text="save",width=10,height=10,command=saveName())
    saveButton.place(x=screen_width/6,y=screen_height/4)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()

def saveName():
    global nameEntry
    global SERVER
    global nameWindow
    global playerName

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def createTicket():
    global gameWindow
    global ticketGrid
    # Ticket Frame
    mianLable = Label(gameWindow, width=65, height=16,relief='ridge', borderwidth=5, bg='white')
    mianLable.place(x=95, y=119)

    xPos = 105
    yPos = 130
    for row in range(0, 3):
        rowList = []
        for col in range(0, 9):
            if(platform.system() == 'Darwin'):
                # For Mac users
                boxButton = Button(gameWindow,
                font = ("Chalkboard SE",18),
                borderwidth=3,
                pady=23,
                padx=-22,
                bg="#fff176", # Initial Yellow color
                highlightbackground='#fff176',
                activebackground='#c5e1a5') # onPress Green Color


                boxButton.place(x=xPos, y=yPos)
            else:
                # For windows users
                boxButton = tkinter.Button(gameWindow, font=("Chalkboard SE",30), width=3, height=2,borderwidth=5, bg="#fff176")
                boxButton.place(x=xPos, y=yPos)

            rowList.append(boxButton)
            xPos += 64
        # Creating nested array
        ticketGrid.append(rowList)
        xPos = 105
        yPos +=82

def placeNumbers():
    for row in range(0,3):
        randomColList = []
        counter = 0
        # getting random 5 cols
        while counter<=4:
            randomCol = random.randint(0,8)
            if(randomCol not in randomColList):
                randomColList.append(randomCol)
                counter+=1


    