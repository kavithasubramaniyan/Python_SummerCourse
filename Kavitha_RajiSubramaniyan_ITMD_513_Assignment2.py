#Get input choice from user
print("1.English Units  2.Metric Units")
choice=int(input("Enter the choice:"))
#If choice =1,calculate BMI in english units
if(choice==1):
#BMI calculation
    height_inch=float(input("Enter the height in inches:"))
    weight_pound=float(input("Enter the weight in pounds:"))
    BMI=(weight_pound*703/(height_inch*height_inch))
    print(round(BMI,1))#Printing BMI
#If choice is 2 then execute the below statement
elif(choice==2):
#BMI calculation    
    height_metr=float(input("Enter the height in meters:"))
    weight_kg=float(input("Enter the weight in kilograms:"))
    BMI=(weight_kg/(height_metr*height_metr))
    print(round(BMI,1))#Printing BMI value
#If choice is not equal to 1 and 2,then execute the else part
else:
    print("Not a valid choice")
#Checking BMI value
if(BMI>=18.5 and BMI<=24.9):
    print("The person is Normal")
#Checking if BMI value is less than 18.5
elif(BMI<18.5):
    print("The person is underweight")
#Checking if BMI value is between 25 and 29.9
elif(BMI>=25.0 and BMI<=29.9):
    print("The person is overweight")
#Executing the else part if none of the above condition is satisfied
else:
    print("The person is obese")
