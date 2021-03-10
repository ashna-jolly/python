class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = rectangle(a, b)
c = int(input("Enter length of rectangle: "))
d = int(input("Enter breadth of rectangle: "))
obj1 = rectangle(c,d)
print("Area of rectangle 1:", obj.area())

print("Perimeter of rectangle 1: ",obj.perimeter())
print("Area of  2nd rectangle:", obj1.area())
print("Perimeter of 2nd rectangle: ",obj1.perimeter())
rect1 = obj.area()
rect2 = obj1.area()
if(rect1 < rect2):
    print("Area of the rectangle 1 is less than the rectangle 2")
else:
    print("Area of the rectangle 1 is greater than the rectangle 2")