# Open the file
numtext = open('numbers.txt', 'r')

# convert to int
number = int(numtext.readline())
total = 0
counter = 0


# add each line to the total. new TOTAL is equal to old total plus number
for line in numtext:
    number = int(line)
    total += number
    print(number)
print("Your total is:\n",total)
      

numtext.close()
    
