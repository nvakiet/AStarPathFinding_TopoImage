from a_star import *
from evaluation import h_Euclidean, h_Manhattan3D, h_Octile3D

def main():
    inPath = "input/map.bmp"
    outPath = ["output/map1.bmp", "output/output1.txt"]
    print("Building graph...")
    graph = Graph(inPath, outPath, (74,213), (96,311), 10)
    print("Searching for path...")
    result = A_Star_Search(graph, h_Euclidean)
    if result == True:
        print("Path has been found, please check output path.")
    else:
        print("No path found. Try increasing m.")

if __name__ == "__main__":
    main()