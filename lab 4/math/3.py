import math

def polygon_area():
    
    area = (n * S**2) / (4 * math.tan(math.pi / n))
    return area


n = int(input())
S = float(input())

# Calculate the area
area = polygon_area()

# Output the area
print(f"The area of the polygon is: {int(area)} ")

