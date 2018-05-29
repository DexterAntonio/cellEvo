

from evolutionClasses import * 
from tkinter import Tk, Canvas

root = Tk()


numXspaces = 2
numYspaces = 1
canWidth = 1000
canHeight = 500

gridSizeX = canWidth//numXspaces 
gridSizeY = canHeight//numYspaces 
xStart = 0
yStart =  0
xLast = xStart
yLast = yStart 


canvas = Canvas(root,width=canWidth,height=canHeight)
canvas.pack() 



list_of_pos = []
for i in range(0,canWidth//gridSizeX):
	xNext = xLast+gridSizeX 
	for j in range(0,canHeight//gridSizeY):
		yNext = yLast+gridSizeY
		recPos =  CellPos(xLast,yLast,xNext,yNext)
		#canvas.create_rectangle(xLast,yLast,xNext,yNext,fill="red")

		list_of_pos.append(recPos)
		yLast = yNext
	xLast = xNext
	yLast = xStart


recTest = []

for rec in list_of_pos:
	#print("rec.xPosS",rec.xPosS,"rec.yPosS",rec.yPosS,"rec.xPosE",rec.xPosE,"rec.yPosE",rec.yPosE)
	rec.drawSelf(canvas)

	#blackLine = canvas.create_line(0,0,200,50)

	#greenBox = canvas.create_rectangle(25,25,130,60,fill="green")

#@canvas.delete(blackLine)
root.mainloop()

#@canvas.delete(blackLine)



