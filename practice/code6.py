import numpy as np
students = np.random.randint(1,101,5000)
students = np.sort(students)
percent = int(input("Enter the percentage of students you want to see: "))
percent = (percent/100) * len(students)
for i in range(-1,-int(percent)-1,-1):
    print((abs(i)),students[i])