import sys#importing sys object to call exit() method
credit_card=(input("Enter your credit card number:"))#Entering card number
credit_card=credit_card.replace(' ','')#If input contains spaces betweene ach 4 digits,then remove it
pwd_dict={"37":"American Express","6":"Discover","5":"MasterCard","4":"Visa"}#Storing the id and password information in dictionary
b=credit_card[0]#Taking first digit
c=credit_card[:2]#Taking first two digits
a=b in pwd_dict.keys() #Checking the value to be present in dictionary
d=c in pwd_dict.keys()#checking the first two digit value to be present in dictionary
if(a==True) and (len(credit_card)>12 and len(credit_card)<17):#first digit in dictionary and length is between 13 and 16
    print("The card type is %s"%(pwd_dict.get(b)))#print statement
elif(d==True)and (len(credit_card)>12 and len(credit_card)<17):#first 2 digit in dictionary and length between 13 and 16
    print("The card type is %s"%(pwd_dict.get(c)))#print statement
else:
    sys.exit("Invalid card type")#system error when input is not valid number
      
length=len(credit_card)#length of card number
count=0#initializing count to 0
pos1=length-1#Calcualting position since it starts from 0
for i in range(length-2,-1,-2):#for loop to calculate from the right most second digit
   # pos=pos1
    sum1=(int(credit_card[i])*2)#Multiply the digit with 2
    #print('Summation is single digit-%d'%sum1)
    if(len(str(sum1))>1):#Checking if length of multiplied variable is greater than1
        number=sum1
        sum2=0#initializing to 0
        while(number>0):#Calculating the sum for the number
            reminder=number%10
            sum2=sum2+reminder
            number=number //10
    
       # print("Sum of numbers for %d sum1 is %d"%(sum1,sum2))
        
        sum1=sum2 
    else:
        sum1=sum1#this part is executed if the multiplied value is single digit
    sum1=sum1+count#Adding summation value
    count=sum1#assigning the summation value to count 
   # pos1=pos-1
print("Total sum of number is %d"%sum1)#print total sum
count=0#initializing count to 0
for i in range(length-1,0,-2):#for loop to take from end of card number
    
    sum3=int(credit_card[i])+count#Adding the integers
    count=sum3#Assigning this summed value to count
   # pos1=pos-1
print("Total sum of number is %d"%sum3)#summation of left over digits
Total=sum1+sum3
print("Final total is %d"%Total)#summation of all the digits in card number
if( Total % 10==0):#taking mod of total value
    print("Card Number is valid-it is divisible by 10")#printing value
else:
    print("Card number is invalid-not divisible by 10")#printing value
