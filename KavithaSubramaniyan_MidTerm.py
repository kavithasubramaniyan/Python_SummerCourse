import random
import string
inp=input("Do you like to generate password?Enter Yes or No" )
if (inp=='Yes'):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digit=string.digits
    symbol=string.punctuation
    full_chars=lower+upper+digit+symbol
    str_concat=''
    minimum=5
    maximum=15
    ran_num = random.randint(minimum, maximum)
    for i in range(ran_num):
        rand=random.choice(full_chars)
        str_concat=str_concat+str(rand)
    #print(str_concat)
    length=len(str_concat)
    if(length>=8):
        print("password contains minimum 8 characters")
        print("The length of the password is:%d"%(length))
        if any(char in lower for char in str_concat):
            print ("Lowercase character is present in password")
    
        else:
            print("No lowercase character present in password")
        
        if any(char in upper for char in str_concat):
            print("Uppercase character is present in password")
        else:
            print("No uppercase character present in password")

        if any(char in symbol for char in str_concat):
            print ("Special character is present in password")
    
        else:
            print("No special character present in password")
        
        if any(char in digit for char in str_concat):
            print ("Number is present in password")
    
        else:
            print("No number is present in password")
        
        print("Password generated successfully")
        print("Your password is %s"%(str_concat))
    else:
        print("Password length is not met.It is less than 8")
        print("Invalid password generated is %s"%(str_concat))
else:
    print("User did not want to generate a password")
