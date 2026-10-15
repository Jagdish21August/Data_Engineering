number_list=[100,200,300,100,200,300,500,800,700,1000]
max_number=0
for i in range(len(number_list)):
    if number_list[i] > max_number:
        max_number = number_list[i]
   
print(f"The maximum number in the list is: {max_number}")   