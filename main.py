from a_star import *
from evaluation import h_Euclidean, h_Manhattan3D, h_Octile3D
import re

def main():
    inPaths = input("Enter image and text input paths (separated by space): ").split()
    outDir = input("Enter output directory (including '/' at the end): ")
    infile = open(inPaths[1], "r")
    start = tuple(map(int, infile.readline().strip("()\n").split(";")))
    goal = tuple(map(int, infile.readline().strip("()\n").split(";")))
    m = int(infile.readline().strip("\n"))

    print()
    hname1 = "Euclidean Distance"
    outfiles_1 = [outDir + "map1.bmp", outDir + "output1.txt"]
    print(f"Building graph for {hname1} heuristic...")
    graph = Graph(inPaths[0], outfiles_1, start, goal, m)
    print("Searching for path...")
    result = A_Star_Search(graph, h_Euclidean)
    if result == True:
        print(f"Path has been found using {hname1} heuristic.")
    else:
        print(f"No path found using {hname1} heuristic.")

    print()
    hname2 = "3D Manhattan Distance"
    outfiles_2 = [outDir + "map2.bmp", outDir + "output2.txt"]
    print(f"Building graph for {hname2} heuristic...")
    graph = Graph(inPaths[0], outfiles_2, start, goal, m)
    print("Searching for path...")
    result = A_Star_Search(graph, h_Manhattan3D)
    if result == True:
        print(f"Path has been found using {hname2} heuristic.")
    else:
        print(f"No path found using {hname2} heuristic.")

    print()
    hname3 = "3D Octile Distance"
    outfiles_3 = [outDir + "map3.bmp", outDir + "output3.txt"]
    print(f"Building graph for {hname3} heuristic...")
    graph = Graph(inPaths[0], outfiles_3, start, goal, m)
    print("Searching for path...")
    result = A_Star_Search(graph, h_Octile3D)
    if result == True:
        print(f"Path has been found using {hname3} heuristic.")
    else:
        print(f"No path found using {hname3} heuristic.")

if __name__ == "__main__":
    main()