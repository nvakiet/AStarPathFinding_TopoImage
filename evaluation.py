from math import sqrt
from typing import Callable
from graph import Graph, detail

def calcPathCost(currentPoint: tuple, nextPoint: tuple) -> float:
    """Calculate the path distance between 2 points on the topographic image

    Args:
        currentPoint (tuple): A tuple (x,y,a) represents the coordinate of the current point on the map
        nextPoint (tuple): A tuple (x,y,a) represents the coordinate of the next point to go on the map

    Returns:
        float: Path distance between 2 points
    """
    dx = nextPoint[0] - currentPoint[0]
    dy = nextPoint[1] - currentPoint[1]
    da = currentPoint[2] - currentPoint[2]
    sgn = 0
    if da < 0:
        sgn = -1
    if da > 0:
        sgn = 1
    return sqrt(dx * dx + dy * dy) + (0.5 * sgn + 1) * abs(da)

def h_Euclidean(nextPoint: tuple, goal: tuple) -> float:
    """Heuristic function using the Euclidean distance between next point and goal point,
    using the (x,y,a) as coordinates in 3D space

    Args:
        nextPoint (tuple): A tuple (x,y,a) represents the coordinate of the next point to go on the map
        goal (tuple): A tuple (x,y,a) represents the coordinate of the goal point

    Returns:
        float: Heuristic value based on Euclidean distance
    """
    dx = goal[0] - nextPoint[0]
    dy = goal[1] - nextPoint[1]
    da = goal[2] - nextPoint[2]
    return sqrt(dx * dx + dy * dy + da * da)

def h_Manhattan3D(nextPoint: tuple, goal: tuple) -> float:
    """Heuristic function using the 3D Manhattan distance between next point and goal point,
    using the (x,y,a) as coordinates in 3D space

    Args:
        nextPoint (tuple): A tuple (x,y,a) represents the coordinate of the next point to go on the map
        goal (tuple): A tuple (x,y,a) represents the coordinate of the goal point

    Returns:
        float: Heuristic value based on 3D Manhattan distance
    """
    dx = abs(goal[0] - nextPoint[0])
    dy = abs(goal[1] - nextPoint[1])
    da = abs(goal[2] - nextPoint[2])
    return float(dx + dy + da)

def h_Octile3D(nextPoint: tuple, goal: tuple) -> float:
    """Heuristic function using the 3D Octile distance between next point and goal point,
    using the (x,y,a) as coordinates in 3D space

    Args:
        nextPoint (tuple): A tuple (x,y,a) represents the coordinate of the next point to go on the map
        goal (tuple): A tuple (x,y,a) represents the coordinate of the goal point

    Returns:
        float: Heuristic value based on 3D Octile distance
    """
    dx = abs(goal[0] - nextPoint[0])
    dy = abs(goal[1] - nextPoint[1])
    da = abs(goal[2] - nextPoint[2])
    deltas = [dx, dy, da]
    deltas.sort()
    return dx + dy + da - (3 - sqrt(3)) * deltas[0] - (2 - sqrt(2)) * deltas[1]

def evaluate(stateSpace: Graph, current: tuple, next: tuple, heuristic: Callable[[tuple, tuple], float]) -> float:
    """Evaluate the total heuristic value of a child cell from the current cell.
    The total heuristic is f = g + h, for g is the child's accumulated path cost/distance and h is the value of the heuristic function at that child cell.

    Args:
        stateSpace: The class containing problem details and graph/matrix to traverse
        current (tuple): Coordinate (x,y) of current cell
        next (tuple): Coordinate (x,y) of child cell
        heuristic (Callable[[tuple, tuple], float]): Heuristic function to calculate heuristic between child cell and goal

    Returns:
        float: Total heuristic point for the child cell
    """
    currentPoint = current + tuple([stateSpace.getPixelValue(current)])
    nextPoint = next + tuple([stateSpace.getPixelValue(next)])
    goalXY = stateSpace.getGoal()
    goalPoint = goalXY + tuple([stateSpace.getPixelValue(goalXY)])
    return stateSpace.getDetails(current).pathTraveled + calcPathCost(currentPoint, nextPoint) + heuristic(nextPoint, goalPoint)