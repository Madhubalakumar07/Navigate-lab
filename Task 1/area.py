
import math
qestion = input("Enter rectangle or circle (r/c): ").strip().lower()
if qestion == 'r':
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print("The area of the rectangle is:", area)
    print("The perimeter of the rectangle is:", perimeter)  
elif qestion == 'c':
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    print("The area of the circle is:", area)
    print("The circumference of the circle is:", circumference)