class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX=0, initY=0):
        """ Create a new point at the origin """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5

    def distanceFromPoint(self, target):
        distx = self.x - target.x
        disty = self.y - target.y
        return (distx**2 + disty**2)**0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        return Point(self.x, -self.y)

    # stuff to run always here such as class/def
def main():
    p = Point(7,6)     # Instantiate an object of type Point
    q = Point()     # and make a second Point

    print(p.getX())
    print(p.getY())

    print(q.getX())
    print(q.getY())

    print(p.distanceFromOrigin())

    print(p.distanceFromPoint(q))
    print(p.reflect_x())

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
