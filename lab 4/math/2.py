
def trapezoid_area():
    area= height*((a+b)/2)
    return area


height=float(input("height: "))
a=float(input("Base, first value: "))
b=float(input("Base, second value: "))

area=trapezoid_area()
print("Expected Output: ", area)