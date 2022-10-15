import math

def paint_calc(height, width, coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    return f"You'll need {number_of_cans} cans of paint."

print(paint_calc(2,4,5))
