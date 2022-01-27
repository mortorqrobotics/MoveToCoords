from tkinter import *  
from PIL import ImageTk,Image  
from networktables import NetworkTables

root = Tk()  
root.title("2022 Field Mapper")
root.iconbitmap("favicon.ico")

NetworkTables.initialize(server='roborio-1515-frc.local')
map = NetworkTables.getTable('FRCMap')

field = Image.open("Gamefield.png")
w, h = field.size

canvas = Canvas(root, width=w, height=h)  
canvas.pack()  
img = ImageTk.PhotoImage(field)  
canvas.create_image(0, 0, anchor=NW, image=img) 

initalX = initalY = 0
fieldWidth = 1646 # cm
fieldHeight = 823 # cm
      
def setInital(event):
    initalX = (event.x / w) * fieldWidth
    initalY = (event.y / h) * fieldHeight

    map.putNumber('initalX', initalX)
    map.putNumber('initalY', initalY)

def moveToCoords(event):
    x = (event.x / w) * fieldWidth
    y = (event.y / h) * fieldHeight
    
    map.putNumber('newX', x)
    map.putNumber('newY', y)

root.bind("<Button-1>", moveToCoords)
root.bind("<Button-3>", setInital)
root.mainloop() 