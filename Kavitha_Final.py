import re
vowels = 0
consonants = 0
dict_vowel = {'a':0}
dict_cons = {'b':0}
with open('cons.dat','r') as file: 
   
    # reading each line     
    for line in file: 
   
        # reading each word         
        for word in line.split(): 
   
             #print(word)
            

            for a in word:
                 if re.match("^[aeiou]+$",a.lower()):

                    if a.lower() in dict_vowel.keys():
                        dict_vowel[a.lower()] = dict_vowel[a.lower()] + 1
                    else:
                        dict_vowel[a.lower()] = 1
                 elif a.isalpha():
                    if a.lower() in dict_cons.keys():
                        dict_cons[a.lower()] = dict_cons[a.lower()] + 1
                    else:
                        dict_cons[a.lower()] = 1

print("vowels_count")

for k,v in dict_vowel.items():
    print(k ,":" ,v)

print("consonants_count")

for k,v in dict_cons.items():
    print(k ,":" ,v)
