# Code written by Chooi Fei Ng
class Rectangle:
    def __init__(self,width,height):
        # Initialise name, width and height of object
        #self.name = name
        self.width = width
        self.height = height

    def set_width(self, width):
        # Set width of shape
        self.width = width

    def set_height(self, height):
        # Set height of shape
        self.height = height

    def get_area(self):
        # Calculate the area of the shape
        return self.width * self.height

    def get_perimeter(self):
        # Calculate the perimeter of the shape
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        # Return the diagonal
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Initialise the line
        line = ''
        if (self.height > 50 or self.width > 50):
            # Check whether the height or width is more than 50. If more than 50, return string stating the picture is
            # too big
            return "Too big for picture."
        else:
            # Print the picture
            height = self.height
            for i in range(height):
                # The total lines is the height of the shape
                # The number of * is the width of the shape
                line = line + '*'*self.width + '\n'
            # Return the picture
            return line

    def __str__(self):
        # Print the width and height of the rectangle
        return "Rectangle(width=%i, height=%i)" %(self.width,self.height)

    def get_amount_inside (self,object):
        # Determines the number of times a shape passed could fit inside the shape
        number = self.get_area()/object.get_area()
        return int(number)


class Square(Rectangle):
    def __init__(self,wh):
        # Inherit all properties of the rectangle
        Rectangle.__init__(self,wh,wh)

    def __str__(self):
        # Print the width of the square
        return "Square(side=%i)" %(self.width)

    def set_side(self,wh):
        # Set the width of the square
        self.width = wh
        self.height = wh