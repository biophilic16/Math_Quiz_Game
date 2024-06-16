import random
import time

print("\n----->MATHS QUIZ<-----\n")
trial=int(input("Number of questions? "))       #number of questions needed
operators=["+","-","*"]         #operators used in expressions    

#function to generate random expression
def generate_exp():
    left=random.randint(1,10)
    right=random.randint(1,10)
    operator=random.choice(operators)
    expr=str(left)+" "+operator+" "+str(right)
    answer=eval(expr)
    return expr,answer

input("Press ENTER to start")
print()
print("   TIME STARTS NOW!")
print("----------------------")

#starting time
start_time=time.time()  

#loop to iterate number of questions
wrong=trial  
for i in range(trial):
    expr,answer=generate_exp()
    while True:
        ans=input("Problem #"+str(i+1)+": "+expr+" = ")
        if ans==str(answer):
            break
        wrong-=1 #for wrong answer accuracy is reduced by one

#ending time
end_time=time.time()    
print("----------------------")

#to check n print accuracy
if wrong<0:
    print("    Accuracy: "+"0"+"/"+str(trial))
else:
    print("    Acurracy: "+str(wrong)+"/"+str(trial))    

print("     Time: "+str(round(end_time-start_time,2))+"s\n")   
print("\t\b BREAK YOUR TIMING NEXT TIME :)\n") 





