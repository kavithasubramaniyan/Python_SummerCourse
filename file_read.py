empFile = open("Employees.txt", "r")
line = empFile.readlines()
print(line)
for i in line:
    a=i.split(' ')
    print(a)
    rate=int(float(a[2]))
    hours=int(float(a[3]))
    print(type(rate))
    print(int(float(rate)))
    print(type(hours))
    print(int(float(hours)))
    print(rate)
    print(hours)
    gross_pay=int(float(rate))*int(float(hours))
    print(gross_pay)
    #To check overtime
    if(hours>40):
        overtime=(40*rate)+((hours-40)*(rate/2))
        print(overtime)
    else:
        print('No overtime pay')
        
        
        
    
