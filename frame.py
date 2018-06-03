import numpy as np 

from evolutionClasses import * 
from tkinter import Tk, Canvas,W

root = Tk()

#user can alter these to change the number of spaces in the grid
numXspaces = 3
numYspaces = 3

#user can change these to change the canvas width and height 
canWidth = 1000
canHeight = 500

#calculated for following forloops 
gridSizeX = canWidth//numXspaces 
gridSizeY = canHeight//numYspaces 
xStart = 0
yStart =  0
xLast = xStart
yLast = yStart 




#creates a position object 
#list_of_pos = []
posArray = np.ndarray([numXspaces,numYspaces],dtype=CellPos)

for i in range(0, numXspaces):   #canWidth//gridSizeX):
	xNext = xLast+gridSizeX 
	for j in range(0,numYspaces):   #canHeight//gridSizeY):
		yNext = yLast+gridSizeY
		recPos =  CellPos(xLast,yLast,xNext,yNext)
		#list_of_pos.append(recPos)
		posArray[i][j] = recPos
		yLast = yNext
	xLast = xNext
	yLast = xStart


#create canvas and put it on the window 
canvas = Canvas(root,width=canWidth,height=canHeight)
canvas.pack() 

x = 0 #pheduo x 
y = 0 #pheduo y 
#this code fills each surrounding rectangle with their adjacent rectangle addresses
#it also draws each position on the canvas 
for row in posArray:
	for rec in row: 
		#list_of_pos:
		rec.drawSelf(canvas) #draws every rectangle 
		#print("########&&&&&&&&&&&&&&&&&&&&&&&&&")
		#print("cell x = ", x, "y = ",y,"has neighbors")
		for i in range(-1,2):
			for j in range(-1,2):
				#print("x, y,, x+i,y+j were called",x,y,i,j,"(x+i) and (y+j)",(x+i),(x+j))

				if(((x+i>=0) and y+j>=0) and (x+i<numXspaces and y+j<numYspaces) and ((x+i)!=x or (y+j)!=y)):
					#print("(x+i)",(x+i),"(y+j)",(y+j))
					rec.surroundingPos.append(posArray[x+i][y+j])
		x += 1 
	y += 1 
	x = 0 

#create cell 

cell = Cell()
cell.position = posArray[1,1]

cell.drawSelf(canvas)
for i in range(0,100):
	newCell = cell.fission()
	newCell.color="red"
	newCell.drawSelf(canvas)

for row in posArray:
	for pos in row:
		i = 0  
		for cell in pos.cellsOnPos:
			if(i==0):
				maxCell = cell
				i = 1
			else:
				if(maxCell.getFitNum()<cell.getFitNum()):
					maxCell = cell 
		pos.cellsOnPos = [maxCell]
		maxCell.color = "orange"
		maxCell.drawSelf(canvas)



#canvas.delete("all")

root.mainloop()




