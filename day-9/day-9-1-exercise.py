student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

def check_score(score):
    grade = ''
    if score > 90:
        grade = 'Outstading'
    elif score > 80:
        grade = 'Exceeds Expectations'
    elif score > 70:
        grade = 'Acceptable'
    else:
        grade = 'Fail'
    return grade

student_grades = {}

for score in student_scores:
    student_grades[score] = check_score(student_scores[score])

print(student_grades)
