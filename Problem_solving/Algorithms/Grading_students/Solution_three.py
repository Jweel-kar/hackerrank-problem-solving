def gradingStudents(grades):
    # Write your code here

    final_grades = []
    
    for i in grades:
            
        if i >= 38:
            if (i + 1) % 5 == 0:
                final_grades.append(i+1)
                
            elif (i + 2) % 5 == 0:
                final_grades.append(i+2)
                
            else:
                final_grades.append(i)
                
        else:
            final_grades.append(i)
                    
    return final_grades
