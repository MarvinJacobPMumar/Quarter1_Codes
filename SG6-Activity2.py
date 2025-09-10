import math

#Input coordinates
x1 = float(input("Enter X of first point:"))
y1 = float(input("Enter Y of first point:"))

x2 = float(input("Enter X of second point:"))
y2 = float(input("Enter Y of second point:"))


#Calculate and round
dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
dist = round(dist, 2)

#Output
print("The distance between the two points is", dist)
