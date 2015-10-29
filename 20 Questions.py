# Design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list and then display the
# following data:
# •  The lowest number in the list
# •  The highest number in the list
# •  The total of the numbers in the list
# •  The average of the numbers in the list
 
# Create a list with a spot for 20 inputs
number_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Get input for a list up to 20, each input adds +1 to count, 
# using a loop

count = 0
while count < 20:
    n = int(input("Pick a random number"))
    number_list[count] = n
    count += 1
    
# Show the user's input
print(number_list)

# Show off some data
print ("The number of random numbers was: ", len(number_list))
print ("The smallest number was: ", min(number_list))
print ("The biggest number was: ", max(number_list))
print ("The sum was: ", sum(number_list))
print ("The average was: ",(sum(number_list) / 20))


