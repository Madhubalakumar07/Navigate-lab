ang1 = int(input("Enter length of side 1: "))
ang2 = int(input("Enter length of side 2: "))
ang3 = int(input("Enter length of side 3: "))
if ang1 + ang2 > ang3 and ang2 + ang3 > ang1 and ang1 + ang3 > ang2:
    if ang1 == ang2 == ang3:
        print("The triangle is equilateral.")
    elif ang1 == ang2 or ang2 == ang3 or ang1 == ang3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")