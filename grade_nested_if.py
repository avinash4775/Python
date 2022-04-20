'''Calculate Grade using nested if-else '''


score=int(input("Enter the score: "))
grade=''
count=0

if(score>100 and score <0):
    print("Score is not valid")
elif(score<=100):
    grade='S'
    count+=1
    if(score<90):
        grade='A'
        if(score<=80):
            grade='B'
            if(score<=70):
                grade='C'
                if(score<60):
                    grade='D'
                    if(score<=50):
                        grade='U'
if(count==1):
    print("Grade is ",grade)
    
