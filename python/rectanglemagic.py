class rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width

    def __add__ (self,rec2):
        return rectangle(self.length + rec2.length, self.width + rec2.width )


if __name__ == '__main__':

    rec = rectangle(10,2)
    rec2 = rectangle(20,40)
    print (rec + rec2)


### an __init__ method which sets the rectangles height and width
##a __str__ method which returns a string which is an ascii-art drawing of the rectangle
##an __int__ method which returns the rectangle's area