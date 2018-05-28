from tkinter import *
from tkinter import ttk 
numXspaces = 100
numYspaces = 50
canWidth = 1000
canHeight = 500

gridSizeX = canWidth//numXspaces #50
gridSizeY = canHeight//numYspaces 
xStart = 0
yStart =  0
xLast = xStart
yLast = yStart 

root = Tk()
canvas = Canvas(root,width=canWidth, height=canHeight)
canvas.pack() 
for i in range(0,canWidth//gridSizeX):
	xNext = xLast+gridSizeX 
	for j in range(0,canHeight//gridSizeY):
		yNext = yLast+gridSizeY
		canvas.create_rectangle(xLast,yLast,xNext,yNext,fill="green")
		yLast = yNext
	
	xLast = xNext
	yLast = xStart


	#blackLine = canvas.create_line(0,0,200,50)

	#greenBox = canvas.create_rectangle(25,25,130,60,fill="green")

#@canvas.delete(blackLine)
root.mainloop()



