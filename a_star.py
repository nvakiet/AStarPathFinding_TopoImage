from evaluation import evaluate, calcPathCost
from graph import Graph, detail
from frontierQueue import FrontierQueue
from typing import Callable

# Function to perform A* search algorithm on a topographic image
def A_Star_Search(graph: Graph, heuristic: Callable[[tuple, tuple], float]) -> bool:
    # Initialize the frontier
    frontier = FrontierQueue()
    # Add start node to frontier
    initCost = evaluate(graph, graph.start, graph.start, heuristic)
    frontier.push(graph.start, initCost)
    #Loop until get result or fail
    while True:
        # Pop the coordinate with lowest cost from frontier
        cell = frontier.pop()
        # If the coordinate is non-exist -> frontier is empty -> Fail to find a path
        if cell is None:
            return False
        # If the coordinate is the goal, traceback the path and save output
        if cell == graph.getGoal():
            graph.tracePath()
            return True
        # Mark the current coordinate as visited
        graph.getDetails(cell).visited = True
        # Scan for possible moves from the current coordinate
        graph.possibleChild(cell)
        moveList = graph.getDetails(cell).child
        # Loop through the available moves of the current coordinate
        # "nextCell" is the coordinate that the current position can move to
        for nextCell in moveList:
            # Calculate f(n) = g(n) + h(n) for next coordinate
            f = evaluate(graph, cell, nextCell, heuristic)
            # If the next coordinate is not visited or is not in the frontier
            if graph.getDetails(nextCell).visited == False or not frontier.hasItem(nextCell):
                # Mark current coordinate as parent/source of next coordinate
                graph.getDetails(nextCell).parent = cell
                # Update the path that will be traveled by the next coordinate
                current = cell + tuple(graph.getPixelValue(cell))
                next = nextCell + tuple(graph.getPixelValue(nextCell))
                graph.getDetails(nextCell).pathTraveled = graph.getDetails(cell).pathTraveled + calcPathCost(current, next)
                # Push the next coordinate to frontier
                frontier.push(nextCell, f)
            else:
                # If the next coordinate is already in the frontier but the new heuristic is lower
                if frontier.hasItem(nextCell) and f < frontier.getPriority(nextCell):
                    # Mark current coordinate as parent/source of next coordinate
                    graph.getDetails(nextCell).parent = cell
                    # Update the path that will be traveled by the next coordinate
                    current = cell + tuple([graph.getPixelValue(cell)])
                    next = nextCell + tuple([graph.getPixelValue(nextCell)])
                    graph.getDetails(nextCell).pathTraveled = graph.getDetails(cell).pathTraveled + calcPathCost(current, next)
                    # Change the heuristic value of the coordinate in the frontier
                    frontier.push(nextCell, f)