bilinguil_dict={"merry":"god","christmas":"jul","and":"och","happy":"got","new":"nytt","year":"ar"}
j=0
Str="Hii New Year"
str1=Str.lower();
Str2=""
count=0
list1=str1.split(" ")

for i in list1: 
    if(i in bilinguil_dict.keys()):
        Str2=Str2+bilinguil_dict.get(i)+" "
    else:    
        count=1
        break
if count==1:
    print("Not in dictionary")
else:
    print(Str2)    
