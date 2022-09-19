from math import sqrt

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.__y = y
        self.__x = x

    def __str__(self):
        return f"{self.__x}, {self.__y}"

    def distance_coordonnees(self, x : float, y: float):
        return sqrt((self.__x - x)**2 + (self.__y - y)**2)

    def distance_point(self, point : object):
        liste = str(point).split(", ")
        return Point.distance_coordonnees(self, (float(liste[0])), (float(liste[1])))
        #return sqrt((self.__x - float(liste[0]))**2 + (self.__y - float(liste[1]))**2)