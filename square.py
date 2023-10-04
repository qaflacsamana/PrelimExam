class Square:
    def __init__(self, length):
        self.length = length

    # area
    def Area(self):
      l = 4
      areaValue = l * 4
      return areaValue
    def printArea(self):
      myArea = self.Area()
      print ("Area of Square:" + str(self.length) + " is " + str(myArea))

    # perimeter
    def Perimeter(self):
      l = 4
      perimeterValue = l * 2
      return perimeterValue
    def printPerimeter(self):
      myPerimeter = self.Perimeter()
      print ("Perimeter of Square:" + str(self.length) + " is " + str(myPerimeter))

# area
area = Square(4)
area.printArea()

# perimeter
area = Square(4)
area.printPerimeter()

