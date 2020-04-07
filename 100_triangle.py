
#Set it Up 
count = 1 
material = "*"

#Work it Out 
for number in range(100): 
    star_count = material * count
    star_count = star_count.center(100)
    print(star_count) 
    count = count + 1


#Finish 