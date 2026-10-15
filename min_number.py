number_list=[100,200,300,100,200,300,500,800,700,1000]
min_number = number_list[0]
for i in range(len(number_list)):
    if number_list[i] < min_number:
        min_number = number_list[i]
   
print(f"The minimum number in the list is: {min_number}")   