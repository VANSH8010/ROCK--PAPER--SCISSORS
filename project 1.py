import random
user_choice=str(input("Enter your choice:  rock , paper, scissors:"))
l=['rock','paper','scissors']
computer_choice=random.choice(l)
print("computer chose")
print(computer_choice)
if str(computer_choice)==str(user_choice):
    print("its an draw")
elif str(computer_choice)=="paper" and  str(user_choice)=="rock":
    print("computer wins")    
elif str(computer_choice)=="rock" and str(user_choice)=="paper":
    print("user wins")
elif str(computer_choice)=="paper" and str(user_choice)=="scissors":
    print("user wins")  
elif str(computer_choice)=="scissors" and str(user_choice)=="rock":
    print("user wins") 
elif str(computer_choice)=="rock" and str(user_choice)=="scissors":
    print("computer wins")

    