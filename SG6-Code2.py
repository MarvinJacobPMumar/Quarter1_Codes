import math
radius = float(input("Enter radius of circle: "))


#Calculate area and round area to 2 decimal places
area = math.pi * (radius ** 2)
area = round(area, 2)

#Output
print("The area of the circle is:", area)