#Triangle perimeter calculator

#input
import math
x1 = int(input("enter x-coordinate for vertex A:"))
y1 = int(input("enter y-coordinate for vertex A:"))
x2 = int(input("enter x-coordinate for vertex B:"))
y2 = int(input("enter y-coordinate for vertex B:"))
x3 = int(input("enter x-coordinate for vertex C:"))
y3 = int(input("enter y-coordinate for vertex C:"))

# process
# Function to Calculate distance of 2 points
def dist(X1,Y1,X2,Y2):
    length = math.sqrt(((X1 - X2) ** 2) + ((Y1 - Y2) ** 2))
    return(length)

vertex1 = dist(x1, y1, x2, y2)
vertex2 = dist(x1, y1, x3, y3)
vertex3 = dist(x2, y2, x3, y3)

# calculates perimeter
perimeter = vertex1 + vertex2 +vertex3

# output
print("AB = " + str(vertex1))
print("AC = " + str(vertex2))
print("BC = " + str(vertex3))
print("perimeter = " + str(perimeter))