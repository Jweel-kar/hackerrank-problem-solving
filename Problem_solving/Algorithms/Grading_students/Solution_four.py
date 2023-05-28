def gradingStudents(grades):
    # Write your code here

    final_grades = []
    
    for i in grades:

        if i >= 38:

            if i % 5 == 3:
                final_grades.append(i+2)
                
            elif i % 5 == 4:
                final_grades.append(i+1)
                
            else:
                final_grades.append(i)
                
        else:
            final_grades.append(i)
                

    return final_grades
