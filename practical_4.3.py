# Find out the BMI of an person.
Weight = int(input("Enter your weight in kilogram's : "))
Height = int(input("Enter you height in meters : "))

BMI = Weight / (Height**2)

if BMI >= 19 and BMI <= 25 :
    print("The person is healthy.")
    
elif BMI < 19 :
    print("The person is underweighted.")
    
elif BMI > 25 :
    print("The person is overweighted.")
    
else : 
    print("You have entered incorrect input !!. Please try again")