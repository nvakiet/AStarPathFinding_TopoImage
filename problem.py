import PIL
import numpy as np

class detail:
    #default constructor
    def __init__(self):
        #cell's parent
        self.parent = tuple()
        #cell's childs
        self.child = list()
        #interacted checking
        self.interacted = False
        #visited checking
        self.visited = False 
        #g(n)
        self.pathTraveled = 0
        
class problem:
    #constructor
    def __init__(self, inPath, start, goal, m):
        #input image
        self.img = PIL.Image.open(inPath)
        #image for calculation
        self.imgL = self.img.convert("L")
        #initialize pValue 2D-array
        self.pValue = np.ndarray(shape = (self.imgL.size[0], self.imgL.size[1]), dtype = int)
        #copy cells' value
        for y in range (self.imgL.size[0]):
            for x in range (self.imgL.size[1]):
                self.pValue[y, x] = self.imgL.getpixel((x, y))
        #initialize info 2D-array
        self.info = np.ndarray(shape = (self.imgL.size[0], self.imgL.size[1]), dtype = detail)
        #set start cell
        self.start = start
        #set goal cell
        self.goal = goal
        #set value m
        self.m = m;
        #number of interacted cells
        self.interacted = 0
        
    #get pixel value of a cell
    def getPixelValue(self, cell):
        return self.pValue[cell[1], cell[0]]
    
    #get goal cell
    def getGoal(self):
        return self.goal
    
    #get info of a cell
    def getDetails(self, cell):
        return self.info[cell[1], cell[0]]
    
    #child checking
    def checkChild(self, cellA, cellB):
        if abs(cellA[1] - cellB[1]) <= 1 and abs(cellA[0] - cellB[0]) <= 1 and abs(self.getPixelValue(cellA) - self.getPixelValue(cellB)) <= self.m:
            return True
        else:
            return False
    
    #setup possible child
    def possibleChild(self, cell):
        #list of 8 neighbor cells
        A = [(cell[0] - 1, cell[1] - 1),
             (cell[0], cell[1] - 1),
             (cell[0] + 1, cell[1] - 1),
             (cell[0] - 1, cell[1]),
             (cell[0] + 1, cell[1]),
             (cell[0] - 1, cell[1] + 1),
             (cell[0], cell[1] + 1),
             (cell[0] + 1, cell[1] + 1)]
        #traverse to check possible child
        for i in range(8):
            if A[i][0] >= 0 and A[i][0] < self.imgL.size[1] and A[i][1] >= 0 and A[i][1] < self.imgL.size[0] and self.checkChild(cell, A[i]):
                self.pValue.child.append(A[i])