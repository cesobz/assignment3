def areaofshape(length, width):
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    print("Area of shape: ", area)
    

areaofshape(length, width)


def circumcirc(radius):
    PI = 3.14
    radius = int(input("Enter radius of circle: "))
    circumference = 2 * PI * radius
    print("Circumference of your circle is: ", circumference)

circumcirc(radius)