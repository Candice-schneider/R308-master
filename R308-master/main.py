from Point import Point
from Cercle import Cercle

def affiche():
    p1 = Point(1, 0)
    p2 = Point()
    print(p1, p2)
    print(p1.distance_point(p2))
    c1 = (Cercle(2, p1))
    print(c1.tracer())
    return 0


if __name__ == '__main__':
    affiche()
