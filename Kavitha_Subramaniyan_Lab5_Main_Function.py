#with open("Employees.txt","r") as myfile:
#    a=myfile.read() 
#    myfile.close()
import functions
print("Choice Description:1,2,3,4,5,6")
          

input1=int(input("Enter the choice:"))
print("The choice entered is %d"%(input1))

if(input1==1):
    
    functions.printall()
    
elif(input1==2):
    functions.printEmp()
    
elif(input1==3):
    functions.addEmp()
    
elif(input1==4):
    functions.deleteEmp()
    
elif(input1==5):
    functions.modifyEmp()
    
elif(input1==6):
    functions.exitApp()
else:
    print("invalid choice entered")
    
#To find gross pay and overtime pay
print("Overtime Pay Calculation")
input_file=input("Enter the file name for payroll:")
import os
val=os.path.isfile(input_file)
if(val==True):

    empFile=open(input_file,"r")

    line = empFile.readlines()
    line2='\n'
    for i in line:
        a=i.split(' ')
    
        rate=int(float(a[2]))
        hours=int(float(a[3]))
    
        gross_pay=int(float(rate))*int(float(hours))
    
    #To check overtime
        if(hours>40):
            overtime=(40*rate)+((hours-40)*(rate/2))
        
        else:
            overtime='No-overtime'
        print(i.split("\n")[0]+" "+str(gross_pay)+" "+str(overtime)+line2)
else:
    print("!!No payroll file is found!!")
    
        
        
        
    
