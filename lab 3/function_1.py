def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Ввод от пользователя
grams = float(input())
ounces = grams_to_ounces(grams)
print(ounces)