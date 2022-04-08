'''Find number of consonent ,vowel,digit,special character in input string'''

s=input("Enter the string")
vowel="aeiouAEIOU"
cons=0
vow=0
num=0
spec=0
for i in s:
    if i in vowel:
        vow+=1
    elif i.isalpha():
        cons+=1
    elif i.isdigit():
        num+=1 
    else:
        spec+=1

print("No of vowel=",vow)  
print("No of consonent=",cons)  
print("No of number=",num)  
print("No of special character=",spec) 
