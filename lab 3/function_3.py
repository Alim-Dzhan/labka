def solve(numheads, numlegs):
    x = (4 * numheads - numlegs) // 2  # chickens
    y = numheads - x  
    return f"Num of chickens: {x} \nNum of rabbits: {y}"

print(solve(35,94))