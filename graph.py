from PIL import Image, ImageDraw
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
        self.pathTraveled: float = 0
        
class Graph:
    #constructor
    def __init__(self, inPath, outPath, start, goal, m):
        #input image
        self.img = Image.open(inPath)
        #image for calculation
        self.imgL = self.img.convert("L")
        #initialize pValue 2D-array
        self.pValue = np.asarray(self.imgL)
        #initialize info 2D-array
        self.info = [[detail() for i in range(self.img.size[0])] for j in range(self.img.size[1])]
        #set start cell
        self.start = start
        #set goal cell
        self.goal = goal
        #set value m
        self.m = m
        #number of interacted cells
        self.totalInteracted = 0
        #List of output paths for saving result, including: bmp result and txt result
        self.outputPath = outPath
        
    #get pixel value of a cell
    def getPixelValue(self, cell):
        return self.pValue[cell[1], cell[0]]
    
    #get goal cell
    def getGoal(self):
        return self.goal
    
    #get info of a cell
    def getDetails(self, cell) -> detail:
        return self.info[cell[1]][cell[0]]
    
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
        #traverse to check possible child and mark the surrounding cells as interacted
        for i in range(8):
            if A[i][0] >= 0 and A[i][0] < self.imgL.size[1] and A[i][1] >= 0 and A[i][1] < self.imgL.size[0]:
                if self.checkChild(cell, A[i]):
                    self.getDetails(cell).child.append(A[i])
                cellInfo = self.getDetails(A[i])
                if cellInfo.interacted == False:
                    cellInfo.interacted = True
                    self.totalInteracted += 1

    #trace back the path from the goal
    def tracePath(self):
        outImg = self.img.convert("RGB")
        drawer = ImageDraw.Draw(outImg, "RGB")
        current = self.getGoal()
        # Loop back to start node
        while len(current) != 0:
            drawer.point(current, (255,0,0))
            current = self.getDetails(current).parent
        outImg.save(self.outputPath[0])
        outfile = open(self.outputPath[1], "w")
        outfile.write(str(self.getDetails(self.getGoal()).pathTraveled) + "\n")
        outfile.write(str(self.totalInteracted) + "\n")
        outfile.close()