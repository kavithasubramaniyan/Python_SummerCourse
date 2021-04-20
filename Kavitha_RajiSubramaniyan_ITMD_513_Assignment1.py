from datetime import datetime#Importing datetime
start_time = datetime.now()#Taking the current time
import pandas as pd#Importing pandas library
import numpy as np#Importing numpy library
from math import sqrt#importing sqrt method from math module
cols=['Appliances','KW/Hr','Annual_Use']#Creating column names for each input we get in run-time
appl_name=[]#Creating list for collecting appliance name
appl_cost=[]#Creating list for collecting cost per KW-hr
appl_usage=[]#Creating list for annual usuage
count=input("Enter the count of appliances:")#Using input function to get input from user
count=int(count)#changing to int type
for i in range(count):#Initializinf for loop from 1 till length of count variable
    appl_name1=input("Please enter the appliance name:")#Input from user for appliance name
    appl_name.append([appl_name1])#Appending the input value to list
    appl_cost1=input("please enter the cost per KW - hr of the appliance (in cents):")#Input from user for cost per KW-hr
    appl_cost.append([appl_cost1])#Appending the input value to list
    appl_ann_usage1=input("please enter the annual usage (in KW - hr):") #Input from user for annual usage
    appl_usage.append([appl_ann_usage1])#Appending input value to list
#Creating dataframe and assigning column names for respective columns
df=pd.DataFrame(np.column_stack([appl_name, appl_cost, appl_usage]),columns=cols)#Using np.column_stack to stack the input as columns to make a single 2D array
df[['KW/Hr','Annual_Use']]=df[['KW/Hr','Annual_Use']].astype(float)#Converting the column type to float
df['total_cost']=df['KW/Hr']*df['Annual_Use']#Multiplying the KW/Hr and Annual_Use columns and assigning to new column 'total_cost'
total_cost_sum=df['total_cost'].sum(axis=0)#Using sum function to find the total of total_cost column
print("Total Annual Cost $%.2f"%(total_cost_sum))#Printing the total annual cost upto two decimal places.
items=len(df)#Finding the length of the dataframe
kw_hr_sum = df['KW/Hr'].sum(axis=0)#Finding the sum of KW/Hr column
#print("The sum of total KW/Hr is %.4f"%(kw_hr_sum).astype(float))
kw_hr_avg=kw_hr_sum/items#Finding the average ofkw_hr column
print("Average $%.4f"%kw_hr_avg)#Printing the average
df['Variance']=pow((kw_hr_avg-df['KW/Hr']),2)#Finding the variance and assigning value to variance column
variance_sum=df['Variance'].sum(axis=0)#Taking the sum function and applying for variance column
variance=variance_sum/items#Taking the variance_sum and dividing by length of dataframe
print("Variance $%.4f"%(variance).astype(float))#Printing variance value
print("Standard deviation $%.4f"%(sqrt(variance)))#Printing standard deviation

end_time = datetime.now()#Taking current time
print('Duration: {}'.format(end_time - start_time))#Printing the run time of the program
