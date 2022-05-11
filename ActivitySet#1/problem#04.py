# Conditional Execution

#3.2
hrs =float(input("Enter Hours: "))
rate=float(input("Enter the rate: "))

if (hrs<=40):
    print(hrs*rate)
elif (hrs>40):
    print(40*rate+(hrs-40)*1.5*rate)




#3.3
score =float(input("Enter Score: "))
if(score<=1.0 and score>=0.0):
    if(score>=0.9):
        print("A")
    elif(score<0.9 and score>=0.8):
        print("B")
    elif(score<0.8 and score>=0.7):
        print("C")
    elif(score<0.7 and score>=0.6):
        print("D")
    elif(score<0.6):
        print("F")
    else:
        print("The score you've entered is wrong")