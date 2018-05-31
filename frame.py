import numpy as np 

from evolutionClasses import * 
from tkinter import Tk, Canvas

root = Tk()


numXspaces = 3
numYspaces = 3
canWidth = 1000
canHeight = 500

gridSizeX = canWidth//numXspaces 
gridSizeY = canHeight//numYspaces 
xStart = 0
yStart =  0
xLast = xStart
yLast = yStart 





list_of_pos = []
posArray = np.ndarray([numXspaces,numYspaces],dtype=CellPos)
for i in range(0,5):
	print("################################################")

for i in range(0, numXspaces):   #canWidth//gridSizeX):
	xNext = xLast+gridSizeX 
	for j in range(0,numYspaces):   #canHeight//gridSizeY):
		yNext = yLast+gridSizeY
		recPos =  CellPos(xLast,yLast,xNext,yNext)
		list_of_pos.append(recPos)
		posArray[i][j] = recPos
		yLast = yNext
	xLast = xNext
	yLast = xStart



canvas = Canvas(root,width=canWidth,height=canHeight)
canvas.pack() 

x = 0 #pheduo x 
y = 0 #pheduo y 
for row in posArray:
	for rec in row:
		#list_of_pos:
		rec.drawSelf(canvas)

		for i in range(-1,2):
			for j in range(-1,2):
				print("x, y,, x+i,y+j were called",x,y,i,j,"(x+i) and (y+j)",(x+i),(x+j))

				if((x+i>=0 and y+j>=0) and (x+i<numXspaces and y+j<numYspaces) and (i!=0 and j!=0)):
					print("(x+i)",(x+i),"(y+j)",(y+j))
					rec.surroundingPos.append(posArray[x+i][y+j])
		x += 1 
	y += 1 




print(len(posArray[2][2].surroundingPos))
#for pos in posArray[2][2].surroundingPos:
#	print("pos is",pos)

print()
root.mainloop()

#@canvas.delete(blackLine)



