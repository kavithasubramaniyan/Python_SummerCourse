import pandas as pd#Importing pandas package
import numpy as np#Importing numpy package
df=pd.DataFrame()#Creating empty dataframe
Month=[]#Creating list for months data
Interest_Amt=[]#Creating list for interest_amt data
Balance=[]#Creating list for balance data
cols=['Month', 'Interest_Amt','Balance']#Creating column names
#Initializing the variable count to 1
count=1
#Setting the while loop with condition count <4
while count<4:
    id=input("Enter the customer id:")#Getting customer id as input from user
    pin=input("Enter the pin:")#Getting pin as input from user
    pwd_dict={"Sam":"Sam123","Sid":"23Sid","Nick":"nick@78","Kavi":"Kavi@1992"}#Storing the id and password information in dictionary
    a=id in pwd_dict.keys() and pin in pwd_dict.values()#Checking if the id and password input combo is present in dictionary
    if(a==True):#Checking if the above condition gives 'True' as output then execute the below statements
        print("Authentication Successful in first attempt .Loggin in")#Print statement
        initial_amt=float(input("Enter the initial deposit amount:"))#Getting initial deposit amount as input from user
        interest_rate=float(input("Enter the rate of interest:"))#Getting rate of interest as input from user
        for i in range(1,13):#initializing for loop to execute 12 times(for 12 onths calculation)
            init_bal=initial_amt+(interest_rate/(100*12))*initial_amt#Calculating the new monthly balance
            init_bal=round(init_bal,2)#Rounding it off to two digits
            print("The ending balance for Month %d is %f"%(i,init_bal))#Printing the new monthly balance for each month
            interest_amt=init_bal-initial_amt#Finding monthly interest amount
            #df=pd.DataFrame([[i,interest_amt,init_bal]],columns = ['Month', 'Interest_Amt','Balance'])
            Month.append([i])#Appending month data to list
            Interest_Amt.append([interest_amt])#Appending interest_amt to list
            Balance.append([init_bal])#Appending balance to list
        
            initial_amt=init_bal#Assigning the new balance as initial amount for the next iteration
            
           
        break#once this for loop gets executed we terminate from loop
    
    else:#When the input condition id and password combo is not present in dictionary
        
        print("Invalid Id or Password.Please try again.%d attempt failed"%(count))#Print message
        count+=1#count incremented to 1
#Converting list to dataframe
df=pd.DataFrame(np.column_stack([Month,Interest_Amt, Balance]),columns=cols)
df['Month']=df['Month'].astype(int)#Changing datatype of month to int
print(df)#Printing the dataframe
