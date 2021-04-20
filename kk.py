with open("Employees.txt","r") as myfile:
    a=myfile.read() 
    myfile.close()

input1=int(input("Enter the choice:"))
print("The choice entered is %d"%(input1))

if(input1==1):
    print("Choice 1 is displaying a gross payroll report for all employees")
    print(a)
elif(input1==2):
    print("Choice 2 is displaying a gross payroll report for just one employee")
    fname=input("Enter the employee first name:")
    lname=input("Enter the employee last name:")
    #print(input2)
    b=fname+" "+lname
    c=a.find(b)
    if(c>=0):
        print("Employee is present in the file")
        file=open("Employees.txt","r")
        line_list = file.readlines()
        file.close()
        line1 = '\n'
        for line in line_list:
                  if b  in line:
                    print("The selected employee details are:")
                    #print(line)
                    line1=line.split(" ")
                    rate=int(float(line1[2]))
                    hours=int(float(line1[3]))
                    gross_pay=int(float(rate))*int(float(hours))
                    print('The gross pay is %f'%(gross_pay))
                    print(line+" "+str(gross_pay))
                     
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
        myfile.write(line+fname+line1+lname+line1+rate+line1+hours)
        myfile.close()
elif(input1==4):
    print("choice 4 is deleting an employee record")
    fname=input("Enter the first name:")
    lname=input("Enter the last name:")
    
    b=fname+" "+lname
    c=a.find(b)
    
    if(c>=0):
        print("Employee is present in the file")
        file=open("Employees.txt","r")
        line_list = file.readlines()
        file.close()
        line1 = '\n'
    
        with open("temp.txt", "w") as myfile1:
             for line in line_list:
                    if b not in line:
                        print(line) 
                        myfile1.write(line1+line)
             myfile1.close()
        
        import os
        try:
                os.remove('Employees.txt')
                print("File Removed!")
        except OSError:
    
              print ('Cannot delete file. Make sure your have enough credentials to delete this file or that no other process is using this file.')
        os.rename('temp.txt','Employees.txt')
        print("File renamed!!")
    else:
        print("Entered employee detail is not present in text file")
elif(input1==5):
    print("choice 5 is modifying an employee record")
    fname=input("Enter the first name:")
    lname=input("Enter the last name:")
    b=fname+" "+lname
    c=a.find(b)
    
    if(c>=0):
        print("Employee is present in the file to modify")
        count=int(input("Enter the number of inputs you going to modify:"))
        if (count==1):
            rh=int(input("Enter 1 for rate and 2 for hours"))
            if(rh==1):
                rate=float(input("Enter the rate to be modified"))
            else:
                hours=float(input("Enter the hours to be modified"))
        elif(count==2):
            rate=float(input("Enter the input for rate"))
            hours=float(input("Enter the input for hours"))
        else:
            print("invalid choice entered to modify")
        file=open("Employees.txt","r")
        line_list = file.readlines()
        file.close()
        line1 = '\n'
        line2=" "
        with open("temp.txt", "w") as myfile2:
            for line in line_list:
                if b in line:
                    if not line.isspace():
                        if((count==1) and (rh==1)):
                            myfile2.write(line1+fname+line2+lname+line2+str(rate))
                        elif((count==1) and (rh!=1)):
                            myfile2.write(line1+fname+line2+lname+line2+str(hours))
                        elif(count==2):
                            myfile2.write(line1+fname+line2+lname+line2+str(rate)+line2+str(hours))
                        else:
                            #myfile2.write(line)
                            print("count is not fetched")
                        
                else:
                    if not line.isspace():
                        myfile2.write(line)
            myfile2.close()
        import os
        try:
                os.remove('Employees.txt')
                print("File Removed!")
        except OSError:
    
              print ('Cannot delete file. Make sure your have enough credentials to delete this file or that no other process is using this file.')
        os.rename('temp.txt','Employees.txt')
        print("File renamed!!")
    else:
        print("Employee is not present in file to modify")
                        
else:
    print("Invalid option entered.Exitting the program")
    print(exit)
    exit()
#To find gross pay and overtime pay
print("Overtime Pay Calculation")
input_file=input("Enter the file name for payroll")
import os
val=os.path.isfile(input_file)
if(val==True):
#empFile = open("Employees.txt", "r")
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
            overtime='NA'
        print(i+" "+str(gross_pay)+" "+str(overtime)+line2)
else:
    print("!!No payroll file is found!!")
    
        
        
        
    
