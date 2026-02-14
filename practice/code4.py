import random
import statistics
from datetime import datetime
import math
data = [random.randint(1,50) for i in range(10)]
print(data)
print(statistics.mean(data))
print(statistics.stdev(data))
print("Generated at: ",datetime.now())



num = 4.6
print(math.floor(num))
num1 = int(input())
num2 = int(input())
print(pow(num1,num2))
lst = list(map(int,input().split()))
print(random.choice(lst))
print(random.choices(lst,k=3))

print(datetime.now().date())