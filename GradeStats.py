# File: GradeStats.py
# Student: Garrett Howard
# UT EID: ghh425
# Course Name: CS303E
# 
# Date: 9/25/2024
# Description of Program: Displays a list of statistics about a number of grades.

print()
def main():
    grade = float(input("Enter a grade or -1 to finish: "))
    
    if grade == -1:
        print ("No Grades Entered.")
        return
    
    numOfGrades = 0
    numOfFailing = 0
    numOfPassing = 0
    gradeSum = 0
    gradeAvg = 0
    gradeMax = grade
    gradeMin = grade
    
    while grade != -1:
        
        numOfGrades += 1
        gradeSum += grade

        if grade < 70:
            numOfFailing += 1
        else:
            numOfPassing += 1

        if (grade > gradeMax) and (grade != -1):
            gradeMax = grade

        if (grade < gradeMin) and (grade != -1):
            gradeMin = grade
        
        gradeAvg = (gradeSum / numOfGrades)
        
        grade = float(input("Enter a grade or -1 to finish: "))

    print()
    print("  Number of grades: ",format(numOfGrades, ">8.0f"))
    print("  Number failing: ",format(numOfFailing, ">10.0f"))
    print("  Number passing: ",format(numOfPassing, ">10.0f"))
    print("  Minimum grade: ",format(gradeMin, ">11.2f"))
    print("  Maximum grade: ",format(gradeMax, ">11.2f"))
    print("  Average grade: ",format(gradeAvg, ">11.2f"))
    print()


main()






    