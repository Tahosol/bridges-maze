from Map import Pixel, empty_map
from State import State

#Shortest path finder
class PathFinder:
    #Constructor
    #tabPixels: table of Pixels objects representing the map of the bridges over the river
    def __init__(self, tabPixels: list):
        self.tabPixels = tabPixels
        self.largeur = len(tabPixels)
        self.hauteur = len(tabPixels[self.largeur-1])
        print(self.largeur, self.hauteur)

    #Finds the shortest path from the start pixel to the end pixel
    #debut: tuple representing the position of the start pixel, fin: tuple representing the position of the end pixel
    #Returns a list of the pixels the path runs through
    def trouver_chemin(self, debut: tuple, fin: tuple) -> list:
        #tupple debut (y,x)
        #tupple fin (y,x)
        distance = dict()
        prec = dict()
        nonvisites = set()
        chemin = []

        for i in range(self.largeur):
            for j in range(self.hauteur):
                distance[(i,j)] = 2147483647
                prec[(i,j)] = None
                nonvisites.add((i,j))
                
        distance[debut] = 0

        print(debut in nonvisites)
        print(nonvisites)
        print("\n")
        print(distance)

        trouve = False
        while (not trouve):
            p = self.__minDistPx(nonvisites, distance)
            print(p)
            nonvisites.remove(p)
            direction = self.tabPixels[p[0]][p[1]].available_bridge_direction()

            if ((len(nonvisites) == 0) or (p == fin)):
                if ((len(nonvisites) == 0) and (distance[fin] == 2147483647)):
                    print("ERREUR!!!")
                else:
                    trouve = True
            else:
                for d in direction:
                    dist = distance[p] + 1
                    if (dist < distance[p]):
                        distance[d] = dist
                        prec[d] = p

        q = fin
        #chemin.append(fin)
        while(q != debut):
            chemin.append(prec[q])
            q = prec[q]
        
        chemin.reverse()

        print(distance[fin])
        print(chemin)

        return chemin

    def __minDistPx(self, nonvisites: set, distance: dict) -> tuple:
        min = 2147483647
        posMin = (-1,-1)
        for p in nonvisites:
            if (distance[p] < min):
                posMin = p
        return posMin

if __name__ == "__main__":
    tab = empty_map(10, 20)
    finder = PathFinder(tab)
    chemin = finder.trouver_chemin((0,0),(12,0))
    print(chemin)
