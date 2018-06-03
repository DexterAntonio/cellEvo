# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 18:16:14 2017

@author: dexter
"""
from tkinter import Tk, Canvas,W

from random import random, randint 
import numpy as np 
import math
from scipy import stats
from scipy.stats import norm

#important classes 
class Gene:
    def __init__(self):
        dnaLength = 10 
        self.dna = ['0']*dnaLength
        self.value = -1
        
class RNA():
    def __init__(self):
        self.valid = False 
        self.rnaList = None
class CellPos():

    def __init__(self,xPosS,yPosS,xPosE,yPosE):
        self.xPosS = xPosS #x position start of rectangle
        self.yPosS = yPosS #y position start of rect
        self.xPosE = xPosE #x position end rect 
        self.yPosE = yPosE #y pos end rect 
        self.surroundingPos = []
        self.color = "green"
        self.antibiotic = "A" #to be implimented 
        self.cellsOnPos = []
    def drawSelf(self,canvas):
        canvas.create_rectangle(self.xPosS,self.yPosS,self.xPosE,self.yPosE,fill=self.color)


    def getAnotherPos(self):
        randPos = randint(0,len(self.surroundingPos)-1)

        return self.surroundingPos[randPos]

class Cell():
    def __init__(self):
        self.gene = Gene()
        self.alive = True 
        self.position = CellPos(0,0,0,0)
        self.color = "blue"
        self.generation = 0
        self.mutationRate = 0.10
        self.ac = ac = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/',' ','d'] #allowed charters
        #to be implimented
        self.fitnessNum = 0
        self.addedToPos = False 

    def addToPosition(self):
        if(not self.addedToPos):
            self.position.cellsOnPos.append(self)

    def fission(self):
        newCell = Cell()
        newCell.gene = replication(self.gene,self.mutationRate,self.ac)
        newCell.alive = True
        newCell.position = self.position.getAnotherPos()
        newCell.color = self.color 
        newCell.generation = self.generation+1 
        newCell.mutationRate = self.mutationRate
        newCell.ac = self.ac 
        return newCell 
    def drawSelf(self,canvas):
        self.addToPosition()
        canvas.create_oval(self.position.xPosS,self.position.yPosS,self.position.xPosE,self.position.yPosE,fill=self.color)
        canvas.create_text((self.position.xPosS+self.position.xPosE)/2,(self.position.yPosS+self.position.yPosE)/2,anchor=W,font="Purisa",text=str(self.getFitNum()))

    def getFitNum(self):
        if(self.fitnessNum>0):
            return self.fitnessNum
        else:
            tmpRNA = transcription(self.gene)
            if(tmpRNA.valid):
                self.fitnessNum = translation(tmpRNA)
                return self.fitnessNum
            else:
                return -1

#important functions
def copyLetter(letter,p,ac): #coppies the letter and occationally puts in a mutation
    if(random()>p):
        return letter
    else:
        return ac[randint(0,len(ac)-1)]
def buildStrFromList(aList,spacer):
    newStr = ""
    for c in aList:
        newStr = newStr + spacer + str(c)
    return newStr
    
def transcription(gene):
    #part 1 combine together number charters into single numbers 
    rnaList = []
    numStack = []
    valid = True 
    j = 0 
    for char in gene.dna:
        if(char in ['1','2','3','4','5','6','7','8','9','0'] and j < 4):
            numStack.append(char)
            j = j + 1 
        else:  
            if not len(numStack) == 0:
                j = 0 
                newStr = ""
                for num in numStack:
                    newStr = newStr+num
                numStack = []
                rnaList.append(newStr)
            if not char == " ":
                rnaList.append(char)
    
    if not len(numStack) == 0: 
        newStr = ""
        for num in numStack:
            newStr = newStr+num
        numStack = []
        rnaList.append(newStr)
    #part 2 identify if its valid reverse polish notation
    #from http://danishmujeeb.com/blog/2014/12/parsing-reverse-polish-notation-in-python/
    stack = []
    for val in rnaList:
        if val in ['+','-','*','/','^','d']:
            if(len(stack)<=1):
                valid = False
                break; 
            stack.pop()
            stack.pop()
            stack.append('10')
        else:
            stack.append('10')
    if(len(stack)==0):
        valid = False 
    newRNA = RNA()
    newRNA.valid = valid 
    newRNA.rnaList = rnaList 
    return newRNA 
    
def translation(rna):
    #assumes that the sequence is valid notation
    stack = [] #adding a zero makes the operations work a lot more often 
    for val in rna.rnaList:
        if val in ['+','-','*','/','^','d']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': 
                if not op1 == 0:
                    result = op2 / op1
                else:
                    result = 0 
            if val=='^': result = op2*op1*1000 #op2 ** op1 power breaks program 
            if val=='d': result = op2*op2*op1*(-1)
            stack.append(result)
        else:
            stack.append(int(val))
            
    return stack.pop() 


#important functions 
def replication(geneOld,p,ac):
    #gene is the gene being duplicated
    #p is the probibility of a random mutation
    geneNew = Gene()
    for i in range(0,len(geneOld.dna)):
        geneNew.dna[i] = copyLetter(geneOld.dna[i],p,ac)
    return geneNew 

def sex(g1,g2,p,ac):
    geneNew = Gene()
    for i in range(0,len(g1.dna)):
        if(round(random())):
            geneNew.dna[i] = copyLetter(g1.dna[i],p,ac)
        else:
            geneNew.dna[i] = copyLetter(g2.dna[i],p,ac)
    return geneNew 
 
def mcSelection(gOld,gNew):
    #print gOld.value 
    #print gNew.value
    #print "----"
    if(gNew.value <= 0 or gOld.value <= 0):
        return gNew.value>=gOld.value 
    else:
        alpha = norm.cdf(math.log(gNew.value)-math.log(gOld.value),0,1)
    
    if(random()<=alpha):#accept the outcome 
      return True 
    return False 