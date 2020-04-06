#User inputs a number and code prints out factors of that number 

user_input = int(input('Please input the value from which you would like to find its factors')) 
count = 1

for numbers in range(user_input): 
    if user_input % count == 0: 
        matching_factor = int(user_input / count)
        print(str(count) + ", " + str(matching_factor)) 
        count = count +1
    else: 
        count = count + 1
