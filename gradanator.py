#
# Author: Alvin Thai
# Description:
#   This program calculates a final course grade based on midterm, final, and homework scores.  It uses input, casting, variable assigning, if/else statements, if/elif/else, order of operations, rounding, while-loop, and boolean true-false conditions. 
# 
def gradanator():
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    print()
    print("Midterm 1: ")
    a = int(input("Weight (0-100)? "))        
    midterm_1_score = int(input("Score earned? "))
    shiftprompt = int(input("Were scores shifted (1=yes, 2=no)? "))    
    if (shiftprompt == 1):
        shift = int(input("Shift amount? "))        
        print("Total points = " + str(midterm_1_score + shift) + " / 100")
        weighted_midterm_1_score = round((int(midterm_1_score + shift) / 100) * a, 1)      
        max_midterm_1_score = a
        if weighted_midterm_1_score >= max_midterm_1_score:
            weighted_midterm_1_score = max_midterm_1_score        
        print("Weighted score = " + str(weighted_midterm_1_score) + "/ " + str(a))
        print()
    else:
        total_points = 100
        if midterm_1_score > total_points:
            midterm_1_score = total_points
        print("Total points = " + str(midterm_1_score) + "/ 100")
        weighted_midterm_1_score = round((int(midterm_1_score) / 100) * a, 1) 
        max_midterm_1_score = a
        if weighted_midterm_1_score >= max_midterm_1_score:
            weighted_midterm_1_score = max_midterm_1_score         
        print("Weighted score = " + str(weighted_midterm_1_score) + "/ " + str(a))
        print()
    print("Midterm 2: ")
    b = int(input("Weight (0-100)? "))
    midterm_2_score = int(input("Score earned? "))
    shiftprompt = int(input("Were scores shifted (1=yes, 2=no)? "))
    if (shiftprompt == 1):
        shift = int(input("Shift amount? "))
        print("Total points = " + str(int(midterm_2_score + shift)) + " / 100")
        weighted_midterm_2_score = round((int(midterm_2_score + shift) / 100) * b, 1)
        max_midterm_2_score = b
        if weighted_midterm_2_score >= max_midterm_2_score:
            weighted_midterm_2_score >= max_midterm_2_score        
        print("Weighted score = " + str(weighted_midterm_2_score) + "/ " + str(b))
        print()
    else:
        print("Total points = " + str(midterm_2_score) + "/ 100")
        weighted_midterm_2_score = round((int(midterm_2_score) / 100) * b, 1)       
        print("Weighted score = " + str(weighted_midterm_2_score) + "/ " + str(b))
        print()
    print("Final: ")
    c = int(input("Weight (0-100)? "))
    final_score = int(input("Score earned? "))
    shiftprompt = int(input("Were scores shifted (1=yes, 2=no)? "))  
    if (shiftprompt == 1):
        shift = int(input("Shift amount? "))
        total_points = 100
        if final_score + shift > total_points:
            final_score = total_points
        print("Total points = " + str(final_score) + "/ 100")
        weighted_final_score = round((int(final_score) / 100) * c, 1)
        max_final_score = c       
        if weighted_final_score > max_final_score:
            weighted_final_score = max_final_score          
        print("Weighted score = " + str(weighted_final_score) + "/ " + str(c))
        print()
    else:
        print("Total points = " + str(final_score) + "/ 100")
        weighted_final_score = round((int(final_score) / 100) * c, 1)       
        print("Weighted score = " + str(weighted_final_score) + "/ " + str(c))
        print()      
    print("Homework: ")
    d = int(input("Weight (0-100)? "))    
    x = int(input("Number of assignments? "))
    count = 1
    score = 0
    maxs = 0
    while count <= x:
        score += int(input("Assignment " + str(count) + " score? "))
        maxs += int(input("Assignment " +str(count) + " max? "))
        count = count + 1
    sections = int(input("How many sections did you attend? "))
    print("Section points = " + str(sections * 3) + " / " + str(34)) 
    print("Total points = " + str(int(sections * 3) + int(score)) + " / " + str(int(maxs) + 34))
    weighted_homework_score = round(((int(sections * 3) + int(score)) / (int(maxs) + 34)) * d, 1)
    max_homework_score = d
    if weighted_homework_score >= max_homework_score:
        weighted_homework_score = max_homework_score
    print("Weighted score = " + str(weighted_homework_score) + " / " + str(d))  
    print()      
    overall_percentage = round(float(weighted_midterm_1_score) + float(weighted_midterm_2_score) + float(weighted_final_score) + float(weighted_homework_score), 1)
    print("Overall percentage = " + str(overall_percentage))
    grade = float(overall_percentage)
    if grade >= 90:
        print("Your grade will at least be: A")
    elif grade >= 80:
        print("Your grade will be at least: B")
    elif grade >= 70:
        print("Your grade will be at least: C")
    elif grade >= 60:
        print("Your grade will be at least: D")
    else:
        print("Your grade will be at least: F")
    print("<< Your custom grade message here >>")
gradanator()