import math

x = float(input("Enter x-coordinate of circle center: "))
y = float(input("Enter y-coordinate of circle center: "))
r = float(input("Enter radius of the circle: "))


px = float(input("Enter x-coordinate of the point: "))
py = float(input("Enter y-coordinate of the point: "))


distance = math.sqrt(math.pow(px-x,2)+math.pow(py-y,2))


if distance < r:
    print("Point lies inside the circle")
elif distance == r:
    print("Point lies on the circle")
else:
    print("Point lies outside the circle")
