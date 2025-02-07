
def sphera_volume(radius):
    volume = (4/3) * 3.1415 * (radius ** 3)
    return volume

radius = float(input("Радиус: "))
print(sphera_volume(radius))

