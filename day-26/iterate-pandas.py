import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

student_df = pandas.DataFrame(student_dict)

# loop through a data frame
for(index,row) in student_df.iterrows():
    print(row)
    if row.student == "Angela":
        print(row.score)