# Handling complex conditions

# First with nested if statements

gpa = float(input("What's your GPA: "))
lowest_grade = float(input("What's your lowest grade: "))

if gpa >= .85:
    if lowest_grade >= .70:
        print("You get a Honour Role")

# Second with the logical expression AND

if gpa >= .85 and lowest_grade >= .70:
    print("You get a Honour Role")

# Handling complex situations with boolean flags
 
if gpa >= .85 and lowest_grade >= .70:
    honour_role = True
else:
    honour_role = False
if honour_role:
    print("You get a Honour Role")

