# create a guess the number game 
secret_number = 5
user_input = int(input("What's the number?"))
prompt = print("I am thinking of a number between 1 and 10")
#Work it out 
print(prompt)
print(user_input)  

if user_input != secret_number:
   while user_input < 1 or user_input > 1: 
       print("invalid input! Please type a number between 1 and 10!") 
       user_input
   while user_input != secret_number:
        print("Try again!")
        user_input  
else: 
    print("Congratulations! You Won!")
    


#Finish