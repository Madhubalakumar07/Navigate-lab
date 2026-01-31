ang1 = int(input("Enter length of side 1: "))
ang2 = int(input("Enter length of side 2: "))
ang3 = int(input("Enter length of side 3: "))
if (ang1>0 and ang2>0 and ang3>0) and (ang1 + ang2 + ang3 == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")