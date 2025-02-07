def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

fahrenheit= float(input())
centigrade =fahrenheit_to_centigrade(fahrenheit)
print(centigrade)