class Square:
    def __int__(self, height="0", width="o"):
        self.height = height
        self.width = width
    @property
    def width(self):
        print("retrieving width")

        return self.__width#protects our data
    @width.setter
    def width(self, value):
        #makes sure a number value is inserted
        if value.isdigit(): #isfloat can work best
            self.__width = value
        else:
            print("enter a number")

    @property
    def height(self):
        print("retrieving height")

        return self.__height#protects our data
    @height.setter
    def height(self, value):
        #makes sure a number value is inserted
        if value.isdigit(): #isfloat can work best
            self.__height = value
        else:
            print("enter a number")

    def getarea(self):
        return int(self.__height)*int(self.__width)
    
def main():
    square = Square()

    height = input("enter height: ")
    width = input("enter width: ")
    square.height = height
    square.width = width

    print("the width is: ",square.width)
    print("the height is: ",square.height)

    print("the area is: ",square.getarea())
main()
