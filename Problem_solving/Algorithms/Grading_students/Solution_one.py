def gradingStudents(grades):
    # Write your code here

    final_grades = []

    for i in grades:

        if i < 38:
            final_grades.append(i)
            
        elif i > 38 and i % 5 == 0:
            final_grades.append(i)
            
        elif i >= 38 and i % 5 != 0:

            if (i + 1) % 5 == 0:
                i = i + 1
                final_grades.append(i)

            elif (i + 2) % 5 == 0:
                i = i + 2
                final_grades.append(i)

            else:
                final_grades.append(i)
                
    return final_grades

