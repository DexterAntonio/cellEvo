
from random import random, randint 
import numpy as np 
import math
from scipy import stats
from scipy.stats import norm

class CellPos():
    def __init__(self,xPosS,yPosS,xPosE,yPosE):
        self.xPosS = xPosS #x position start of rectangle
        self.yPosS = yPosS # y position start of rect
        self.xPosE = xPosE #x position end rect 
        self.yPosE = yPosE #y pos end rect 
        self.surroundingPos = []
        self.color = "green"
        self.antibiotic = "A" #to be implimented 
    def drawSelf(self):
        x = 0 
        #canvas.create_rectangle(self.xPosS,self.XposS,self.xPosE,self.yPosE,fill=self.color)
