#sum = 0
#while sum < 100:
 #   try:
  #      num = int(input("Enter an integer: "))
   #     sum += num
    #except ValueError:
     #   print("Invalid input. Please enter an integer.")
#print("Sum of integers:", sum)



sum = 0
list=[]
while sum < 100:
        num = int(input("Enter an integer: "))
        sum += num
        list.append(num)
print(list)