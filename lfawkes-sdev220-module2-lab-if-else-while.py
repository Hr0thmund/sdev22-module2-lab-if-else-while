# Lee Fawkes
# SDEV 220 50P - Andrew Emily
# lfawkes-sdev220-module2-lab-if-else-while.py
# This app will input a student's last name, quit processing if name entered 
# # is "ZZZ", otherwise then read first name, read GPA as float, test the GPA,
# and if it's 3.75 or above print that the student has made the Dean's list
# if it's 3.5 or above, print that the student has made the honor roll.

# Observations on instructions:
# 1. The instructions don't say whether the student's name needs to be printed
# 2. The instructions aren't clear whether a GPA of 3.5 or high should result
#    in printing both "Dean's List" and "Honor Roll", or just "Dean's List"
# 3. The instructions don't say that the test output needs to be displayed.
#    I did test, but the Visual Studio Code option I'm choosing doesn't
#    show the output. Please let me know if that is not optimal.

last_name = ""

while last_name != "ZZZ":
    last_name = input("Enter student's last name (ZZZ to quit): ")
    if last_name != "ZZZ":
        first_name = input("Enter student's first name: ")
        student_gpa = float(input("Enter the student's GPA: "))
        if student_gpa >= 3.5:
            print(first_name, last_name, "has made the Dean's List.")
        if student_gpa >= 3.25:
            print(first_name, last_name, "has made the Honor Roll.")
            
