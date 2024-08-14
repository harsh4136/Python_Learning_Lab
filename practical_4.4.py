# Write a program to read the marks and assign a grade to astudent. Grading system: A (>=90), B (80-89), C (70-79), D
# (60-69), E (50-59), F (<50). (Use the Switch case)

Marks = int(input("Enter the marks you obtained : "))

if Marks >= 90 :
    print(f"Your marks is {Marks} And your grade is A")

elif Marks >= 80 and Marks <= 89 :
    print(f"Your marks is {Marks} And your grade is B")
    
elif Marks >= 70 and Marks <= 79 :
    print(f"Your marks is {Marks} And your grade is c")
    
elif Marks >= 60 and Marks <= 69 :
    print(f"Your marks is {Marks} And your grade is D")
    
elif Marks >= 50 and Marks <= 59 :
    print(f"Your marks is {Marks} And your grade is E")
    
elif Marks < 50 :
    print(f"Your marks is {Marks} And your grade is F")
    
else :
    print("You have Entered incorrect Marks!! Please try again ....")
