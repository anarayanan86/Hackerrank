import math
ab = int(input())
bc = int(input())
ac = math.sqrt(ab**2 + bc**2)
angle = math.asin(ab/ac)
print(round(math.degrees(angle)), end="")
print('°')