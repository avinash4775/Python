str1=input("Enter the word: ")
str2="ing"
if len(str1)<3:
    print("")
elif str2 in str1:
    print(str1+"ly")
else:
    print(str1+"ing")
