import math
import numpy as np

class detail:
    def __init__(self):
        self.parent = tuple()
        self.child = list()
        self.interacted = False
        self.visited = False 
        self.pathTraveled = 0
        
class problem:
    #constructor
    def __init__(self, xMax, yMax, start, goal, m):
        self.start = start
        self.goal = goal
        self.m = m;
        self.interacted = 0
        self.pValue = np.ndarray(shape = (yMax, xMax), dtype = int, order = 'F')
        self.info = np.ndarray(shape = (yMax, xMax), dtype = detail, order = 'F')  
    #get pixel value of a cell
    def getPixelValue(self, point):
        return self.height[point[0], point[1]]
    #get goal cell
    def getGoal(self):
        return self.goal
    #get info of a cell
    def getDetails(self, point):
        return self.info[point[0], point[1]]
    #check child?
