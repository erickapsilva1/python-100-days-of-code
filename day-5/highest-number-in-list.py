student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

number1 = 0
number2 = 0
max_number = 0

for score in student_scores:
    if max_number < score:
        max_number = score

print(f'The highest score in the class is: {max_number}')
