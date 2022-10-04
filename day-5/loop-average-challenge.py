student_heights = input('Students heights: ').split()

counter = 0
heights = 0

for height in student_heights:
    heights += float(height)
    counter += 1

average = heights / counter

print(f'{round(average,2)}')
