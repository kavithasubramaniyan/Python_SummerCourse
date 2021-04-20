with open("Employees.txt","r") as myfile:
    a=myfile.read() 
    myfile.close()
#print(a)
#print(_)
input1=int(input("Enter the choice:"))
print("The choice entered is %d"%(input1))

if(input1==1):
    print("Choice 1 is displaying a gross payroll report for all employees")
    print(a)
elif(input1==2):
    print("Choice 2 is displaying a gross payroll report for just one employee")
    input2=input("Enter the employee name:")
    print(input2)
    b=a.find(input2)
    if(b>=0):
        print("Employee is present in the file")
    else:
        print("Employee is not present in the file")
elif(input1==3):
    print("Choice 3 is adding an employee record")
    fname=input("Enter the first name:")
    lname=input("Enter the last name:")
    rate=input("Enter the rate:")
    hours=input("Enter the hours:")
    with open("Employees.txt", "a") as myfile:
        line = '\n'
        line1=" "
        myfile.write(fname+line1+lname+line1+rate+line1+hours+line)
        myfile.close()
elif(input1==4):
    print("choice 4 is deleting an employee record")
    fname=input("Enter the first name:")
    lname=input("Enter the last name:")
    #print(input2)
    b=fname+" "+lname
    #text_file = open('temp.txt','w')
    #file=open("Employees.txt","r")
    #line_list = file.readlines()
    #file.close()
    line_list = a.split('\n')
    with open("temp.txt", "w") as myfile1:
        for line in line_list:
            if b not in line:
                print(line) 
                myfile1.write(line)
        myfile1.close()
    
    #file.close()
    #myfile.close()
print("---------------------------------------")
print(type(a))
import os
try:
    os.remove('Employees.txt')
    print("File Removed!")
except OSError:
    
    print ('Cannot delete file. Make sure your have enough credentials to delete this file or that no other process is using this file.')
os.rename('temp.txt','Employees.txt')
print("File renamed!!")